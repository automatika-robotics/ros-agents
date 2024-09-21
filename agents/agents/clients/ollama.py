from typing import Any, Optional

import httpx

from ..models import LLM
from ..utils import encode_arr_base64
from .model_base import ModelClient

__all__ = ["OllamaClient"]


class OllamaClient(ModelClient):
    """An HTTP client for interaction with ML models served on ollama"""

    def __init__(
        self,
        model: LLM,
        host: str = "127.0.0.1",
        port: int = 11434,
        inference_timeout: int = 30,
        init_on_activation: bool = True,
        logging_level: str = "info",
    ):
        self.model: LLM = model
        self.model._set_ollama_checkpoint()
        try:
            from ollama import Client

            self.client = Client(host=f"{host}:{port}")
        except ModuleNotFoundError as e:
            raise ModuleNotFoundError(
                "In order to use the OllamaClient, you need ollama-python package installed. You can install it with 'pip install ollama'"
            ) from e
        super().__init__(
            model=model,
            host=host,
            port=port,
            inference_timeout=inference_timeout,
            init_on_activation=init_on_activation,
            logging_level=logging_level,
        )
        self._check_connection()

    def _check_connection(self) -> None:
        """Check if the platfrom is being served on specified IP and port"""
        # Ping remote server to check connection
        self.logger.info("Checking connection with remote_host Ollama")
        try:
            httpx.get(f"http://{self.host}:{self.port}").raise_for_status()
        except Exception as e:
            self.logger.error(str(e))
            raise

    def _initialize(self) -> None:
        """
        Initialize the model on platform using the paramters provided in the model specification class
        """
        self.logger.info(f"Initializing {self.model.name} on ollama")
        try:
            # set timeout on underlying httpx client
            self.client._client.timeout = self.init_timeout
            r = self.client.pull(self.model.checkpoint)
            if r.get("status") != "success":  # type: ignore
                raise Exception(f"Could not pull model {self.model.checkpoint}")
            if hasattr(self.model, "system_prompt") and (
                sys_prompt := self.model.system_prompt  # type: ignore
            ):
                # create modelfile if a system prompt is given
                modelfile = f'''FROM {self.model.checkpoint}
    SYSTEM """
    {sys_prompt}
    """
    '''
                self.client.create(self.model.checkpoint, modelfile=modelfile)

            # load model in memory with empty request
            self.client.generate(model=self.model.checkpoint, keep_alive=10)
            self.logger.info(f"{self.model.name} model initialized")
        except Exception as e:
            self.logger.error(str(e))
            return None

    def _inference(self, inference_input: dict[str, Any]) -> Optional[dict]:
        """Call inference on the model using data and inference parameters from the component"""
        if not (query := inference_input.get("query")):
            raise TypeError(
                "OllamaClient can only be used with LLM and MLLM components"
            )
        # create input
        input = {
            "model": self.model.checkpoint,
            "messages": query,
        }
        inference_input.pop("query")
        if images := inference_input.get("images"):
            # make images parth of the latest message in message list
            input["messages"][-1]["images"] = [encode_arr_base64(img) for img in images]
            inference_input.pop("images")
        # ollama uses num_predict for max_new_tokens
        if inference_input.get("max_new_tokens"):
            inference_input["num_predict"] = inference_input["max_new_tokens"]
            inference_input.pop("max_new_tokens")
        input["options"] = inference_input

        # call inference method
        try:
            # set timeout on underlying httpx client
            self.client._client.timeout = self.inference_timeout
            ollama_result = self.client.chat(**input)
        except Exception as e:
            self.logger.error(str(e))
            return None

        self.logger.debug(str(ollama_result))

        # Add np images back in inference input
        if images:
            input["images"] = images

        # make result part of the input
        input["output"] = ollama_result["response"]  # type: ignore
        return input

    def _deinitialize(self):
        """Deinitialize the model on the platform"""

        self.logger.error(f"Deinitializing {self.model.name} model on ollama")
        try:
            self.client.generate(model=self.model.checkpoint, keep_alive=0)
        except Exception as e:
            self.logger.error(str(e))
            return None
