from pathlib import Path
from typing import Any, Optional, Union

from jinja2.environment import Template

from ..callbacks import TextCallback
from ..clients.db_base import DBClient
from ..clients.model_base import ModelClient
from ..config import LLMConfig
from ..ros import FixedInput, String, Topic, Detections
from ..utils import get_prompt_template, validate_func_args
from .model_component import ModelComponent


class LLM(ModelComponent):
    """
    This component utilizes large language models (e.g LLama) that can be used to process text data.

    :param inputs: The input topics or fixed inputs for the LLM component.
        This should be a list of Topic objects or FixedInput instances.
    :type inputs: list[Topic | FixedInput]
    :param outputs: The output topics for the LLM component.
        This should be a list of Topic objects. String type is handled automatically.
    :type outputs: list[Topic]
    :param model_client: The model client for the LLM component.
        This should be an instance of ModelClient.
    :type model_client: ModelClient
    :param config: The configuration for the LLM component.
        This should be an instance of LLMConfig. If not provided, defaults to LLMConfig().
    :type config: LLMConfig
    :param db_client: An optional database client for the LLM component.
        If provided, this should be an instance of DBClient. Otherwise, it defaults to None.
    :type db_client: Optional[DBClient]
    :param trigger: The trigger value or topic for the LLM component.
        This can be a single Topic object, a list of Topic objects, or a float value for a timed component. Defaults to 1.
    :type trigger: Union[Topic, list[Topic], float]
    :param callback_group: An optional callback group for the LLM component.
        If provided, this should be a string. Otherwise, it defaults to None.
    :type callback_group: str
    :param component_name: The name of the LLM component.
        This should be a string and defaults to "llm_component".
    :type component_name: str
    :param kwargs: Additional keyword arguments for the LLM.

    Example usage:
    ```python
    text0 = Topic(name="text0", msg_type="String")
    text1 = Topic(name="text1", msg_type="String")
    config = LLMConfig()
    model = Llama3(name='llama')
    model_client = ModelClient(model=model)
    llm_component = LLM(inputs=[text0],
                        outputs=[text1],
                        model_client=model_client,
                        config=config,
                        component_name='llama_component')
    ```
    """

    @validate_func_args
    def __init__(
        self,
        *,
        inputs: list[Union[Topic, FixedInput]],
        outputs: list[Topic],
        model_client: ModelClient,
        config: Optional[LLMConfig] = None,
        db_client: Optional[DBClient] = None,
        trigger: Union[Topic, list[Topic], float] = 1,
        callback_group=None,
        component_name: str = "llm_component",
        **kwargs,
    ):
        self.config: LLMConfig = config or LLMConfig()
        # set allowed inputs/outputs when parenting multimodal LLMs
        self.allowed_inputs = (
            kwargs["allowed_inputs"]
            if kwargs.get("allowed_inputs")
            else {"Required": [String], "Optional": [Detections]}
        )
        self.handled_outputs = [String]
        self._component_template: Optional[Template] = None

        self.db_client = db_client if db_client else None

        super().__init__(
            inputs,
            outputs,
            model_client,
            self.config,
            trigger,
            callback_group,
            component_name,
            **kwargs,
        )

    def activate(self):
        # initialize db client
        if self.db_client:
            self.db_client.check_connection()
            self.db_client.initialize()

        # activate the rest
        super().activate()

    def deactivate(self):
        # deactivate the rest
        super().deactivate()

        # deactivate db client
        if self.db_client:
            self.db_client.check_connection()
            self.db_client.deinitialize()

    @validate_func_args
    def add_documents(
        self, ids: list[str], metadatas: list[dict], documents: list[str]
    ) -> None:
        """Add documents to vector DB for Retreival Augmented Generation (RAG).

        ```{important}
        Documents can be provided after parsing them using a document parser. Checkout various document parsers, available in packages like [langchain_community](https://github.com/langchain-ai/langchain/tree/master/libs/community/langchain_community/document_loaders/parsers)
        ```

        :param ids: List of unique string ids for each document
        :type ids: list[str]
        :param metadatas: List of metadata dicts for each document
        :type metadatas: list[dict]
        :param documents: List of documents which are to be store in the vector DB
        :type documents: list[str]
        :rtype: None
        """

        if not self.db_client:
            raise AttributeError(
                "db_client needs to be set in component for add_documents to work"
            )

        db_input = {
            "collection_name": self.config.collection_name,
            "distance_func": self.config.distance_func,
            "ids": ids,
            "documents": documents,
            "metadatas": metadatas,
        }
        self.db_client.add(db_input)

    def _make_rag_query(self, query: str) -> Optional[str]:
        """Retreive documents for RAG.
        :param query:
        :type query: str
        :rtype: str | None
        """
        if not self.db_client:
            raise AttributeError(
                "db_client needs to be set in component for RAG to work"
            )
        # get documents
        db_input = {
            "collection_name": self.config.collection_name,
            "query": query,
            "n_results": self.config.n_results,
        }
        result = self.db_client.query(db_input)
        if result:
            # add metadata as string if asked
            rag_docs = (
                "\n".join(
                    f"{str(meta)}, {doc}"
                    for meta, doc in zip(
                        result["output"]["metadata"], result["output"]["documents"]
                    )
                )
                if self.config.add_metadata
                else "\n".join(doc for doc in result["output"]["documents"])
            )
            return f"{rag_docs}{query}"
        return query

    def _create_input(self, *_, **kwargs) -> Optional[dict[str, Any]]:
        """Create inference input for LLM models
        :param args:
        :param kwargs:
        :rtype: dict[str, Any]
        """
        # context dict to gather all String inputs for use in system prompt
        context = {}
        # set llm query as trigger
        if trigger := kwargs.get("topic"):
            query = self.trig_callbacks[trigger.name].get_output()
            context[trigger.name] = query
        else:
            query = None

        # aggregate all inputs that are available
        for i in self.callbacks.values():
            if (item := i.get_output()) is not None:
                # set trigger equal to a topic with type String if trigger not found
                if i.input_topic.msg_type is String:
                    if not query:
                        query = item
                    context[i.input_topic.name] = item
                elif i.input_topic.msg_type is Detections:
                    context[i.input_topic.name] = item

        if query is None:
            return None

        # set system prompt template
        query = (
            self._component_template.render(context)
            if self._component_template
            else query
        )
        # add rag docs to query if enabled in config and if docs retreived
        query = self._make_rag_query(query) if self.config.enable_rag else query

        self.get_logger().debug(query)

        return {
            "query": query,
            **self.config._get_inference_params(),
        }

    def set_topic_prompt(self, input_topic: Topic, template: Union[str, Path]) -> None:
        """Set prompt template on any input topic of type string.

        :param input_topic: Name of the input topic on which the prompt template is to be applied
        :type input_topic: Topic
        :param template: Template in the form of a valid jinja2 string or a path to a file containing the jinja2 string.
        :type template: Union[str, Path]
        :rtype: None

        Example usage:
        ```python
        llm_component = LLM(inputs=[text0],
                            outputs=[text1],
                            model_client=model_client,
                            config=config,
                            component_name='llama_component')
        llm_component.set_topic_prompt(text0, template="You are an amazing and funny robot. You answer all questions with short and concise answers. Please answer the following: {{ text0 }}")
        ```
        """
        if callback := self.callbacks.get(input_topic.name):
            if not callback:
                raise TypeError("Specified input topic does not exist")
            if not isinstance(callback, TextCallback):
                raise TypeError(
                    f"Prompt can only be set for a topic of type String, {callback.input_topic.name} is of type {callback.input_topic.msg_type}"
                )
            callback._template = get_prompt_template(template)

    def set_component_prompt(self, template: Union[str, Path]) -> None:
        """Set component level prompt template which can use multiple input topics.

        :param template: Template in the form of a valid jinja2 string or a path to a file containing the jinja2 string.
        :type template: Union[str, Path]
        :rtype: None

        Example usage:
        ```python
        llm_component = LLM(inputs=[text0],
                            outputs=[text1],
                            model_client=model_client,
                            config=config,
                            component_name='llama_component')
        llm_component.set_component_prompt(template="You are an amazing and funny robot. You answer all questions with short and concise answers. You can see the following items: {{ detections }}. Please answer the following: {{ text0 }}")
        ```
        """
        self._component_template = get_prompt_template(template)
