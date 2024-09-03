# Create a Go-to-X component using map data

In the previous [example](semantic_map.md) we created a semantic map using the MapEncoding component. Intuitively one can imagine that using the map data would require some form of RAG. Let us suppose that we want to create a Go-to-X component, which, when given a command like 'Go to the yellow door', would retreive the coordinates of the _yellow door_ from the map and publish them to a goal point topic of type _PoseStamped_ to be handled by our robots navigation system. We will create our Go-to-X component using the LLM component provided by ROS Agents. We will start by initializing the component, and configuring it to use RAG.

```python
from agents.models import Llama3_1
from agents.config import LLMConfig
from agents.clients.ollama import OllamaClient
from agents.ros import Topic

# Start a Llama3.1 based llm component using ollama client
llama = Llama3_1(name="llama")
llama_client = OllamaClient(llama)

# Define LLM input and output topics including goal_point topic of type PoseStamped
llm_in = Topic(name="llm_in", msg_type="String")
llm_out = Topic(name="llm_out", msg_type="String")
goal_point = Topic(name="goal_point", msg_type="PoseStamped")
```

In order to configure the component to use RAG, we will set the following options in its config.

```python
config = LLMConfig(enable_rag=True,
                   collection_name="map",
                   distance_func="l2",
                   n_results=1,
                   add_metadata=True)
```

Note that the _collection_name_ parameter is the same as the map name we set in the previous [example](semantic_map.md). We have also set _add_metadata_ parameter to true to make sure that our metadata is included in the RAG result, as the spatial coordinates we want to get are part of the metadata. Let us have a quick look at the metadata stored in the map by the MapEncoding component.

```
{
    "coordinates": [1, 2],
    "layer_name": "Topic_Name",  # same as topic name that the layer is subscribed to
    "timestamp": 1234567,
    "temporal_change": True
}
```

With this information, we will first initialize our component.
```{caution}
In the following code block we are using the same DB client that was setup in the previous [example](semantic_map.md).
```

```python
# initialize the component
goto = LLM(
    inputs=[llm_in],
    outputs=[llm_out, goal_point],
    model_client=ollama_client,
    db_client=chroma_client,  # check the previous example where we setup this database client
    trigger=llm_in
    component_name='go_to_x'
)
```

Knowing that the output of retreival will be appended to the beggining of our query as context, we will setup a component level promot for our LLM.

```python
# set a component prompt
goto.set_component_prompt(
    template="""From the given metadata, extract coordinates and provide
    the coordinates in the following json format:\n {"position": coordinates}"""
)
```

```{note}
One might notice that we have not used an input topic name in our prompt. This is because we only need the input topic to fetch data from the vector DB during the RAG step. The query to the LLM in this case would only be composed of data fetched from the DB and our prompt.
```

As the LLM output will contain text other than the _json_ string that we have asked for, we need to add a pre-processing function to the output topic that extracts the required part of the text and returns the output in a format that can be published to a _PoseStamped_ topic, i.e. a numpy array of floats.

```python
import json
import numpy as np

# pre-process the output before publishing to a topic of msg_type PoseStamped
def llm_answer_to_goal_point(output: str) -> Optional[np.ndarray]:
    # extract the json part of the output string (including brackets)
    # one can use sophisticated regex parsing here but we'll keep it simple
    json_string = output[output.find("{"):output.find("}") + 1]

    # load the string as a json and extract position coordinates
    # if there is an error, return None, i.e. no output would be published to goal_point
    try:
        json_dict = json.loads(json_string)
        return np.array(json_dict['position'])
    except Exception:
        return

# add the pre-processing function to the goal_point output topic
goto.add_publisher_preprocessor(goal_point, llm_answer_to_goal_point)
```

## Launching the Components

And we will launch our Go-to-X component.

```python
from agents.ros import Launcher

# Launch the component
launcher = Launcher(components=[goto],
                    activate_all_components_on_start=True)
launcher.bringup()
```

And that is all. Our Go-to-X component is ready. The complete code for this example is given below:

```{code-block} python
:caption: Go-to-X Component
:linenos:

import json
import numpy as np
from agents.models import Llama3_1
from agents.config import LLMConfig
from agents.clients.ollama import OllamaClient
from agents.ros import Launcher, Topic

# Start a Llama3.1 based llm component using ollama client
llama = Llama3_1(name="llama")
llama_client = OllamaClient(llama)

# Define LLM input and output topics including goal_point topic of type PoseStamped
llm_in = Topic(name="llm_in", msg_type="String")
llm_out = Topic(name="llm_out", msg_type="String")
goal_point = Topic(name="goal_point", msg_type="PoseStamped")

config = LLMConfig(enable_rag=True,
                   collection_name="map",
                   distance_func="l2",
                   n_results=1,
                   add_metadata=True)

# initialize the component
goto = LLM(
    inputs=[llm_in],
    outputs=[llm_out, goal_point],
    model_client=ollama_client,
    db_client=chroma_client,  # check the previous example where we setup this database client
    trigger=llm_in
    component_name='go_to_x'
)

# set a component prompt
goto.set_component_prompt(
    template="""From the given metadata, extract coordinates and provide
    the coordinates in the following json format:\n {"position": coordinates}"""
)

# pre-process the output before publishing to a topic of msg_type PoseStamped
def llm_answer_to_goal_point(output: str) -> Optional[np.ndarray]:
    # extract the json part of the output string (including brackets)
    # one can use sophisticated regex parsing here but we'll keep it simple
    json_string = output[output.find("{"):output.find("}") + 1]

    # load the string as a json and extract position coordinates
    # if there is an error, return None, i.e. no output would be published to goal_point
    try:
        json_dict = json.loads(json_string)
        return np.array(json_dict['position'])
    except Exception:
        return

# add the pre-processing function to the goal_point output topic
goto.add_publisher_preprocessor(goal_point, llm_answer_to_goal_point)

# Launch the component
launcher = Launcher(components=[goto],
                    activate_all_components_on_start=True)
launcher.bringup()
