### Stateful Graph

 LangGraph revolves around the concept of a stateful graph, where each node in the graph represents a step in your computation, and the graph maintains a state that is passed around and updated as the computation progresses.

### State

:::tip
1. Learn more about [State- Explanation](https://langchain-ai.github.io/langgraph/concepts/low_level/#state)
:::

  1. The State consists of the schema of the graph as well as reducer functions which specify how to apply updates to the state.
  2. State is the shared data structure that represents the current snapshot of your application. It can be any Python type, but is typically a TypedDict or Pydantic BaseModel.
  3. The State schema serves as the input schema for all Nodes and Edges in the graph.

    ```python
    from typing_extensions import TypedDict

    class State(TypedDict):
      graph_state: str
    ```

### Nodes

  1. Node represents a function or a computation step. Nodes are designed to perform specific tasks, such as processing input, making decisions, or interacting with external APIs.
  2. Nodes are nothing but python functions.
  3. Python functions that encode the logic of your agents. They receive the current State as input, perform some computation or side-effect, and return an updated State.
   ```python
    def node_1(state):
        print("---Node 1---")
        return {"graph_state": state['graph_state'] +" I am"}

    def node_2(state):
        print("---Node 2---")
        return {"graph_state": state['graph_state'] +" happy!"}

    def node_3(state):
        print("---Node 3---")
        return {"graph_state": state['graph_state'] +" sad!"}
    ```

### Edges

1. Edges connect the nodes in your graph, defining the flow of computation. 

2. LangGraph supports conditional edges, allowing you to dynamically determine the next node to execute based on the current state of the graph.

:::tip
  1. Learn more about [Edges - explanation](https://langchain-ai.github.io/langgraph/concepts/low_level/#edges)
:::

    ```python
    import random
    from typing import Literal

    def decide_mood(state) -> Literal["node_2", "node_3"]:
        # Often, we will use state to decide on the next node to visit
        user_input = state['graph_state'] 
        # Here, let's just do a 50 / 50 split between nodes 2, 3
        if random.random() < 0.5:
            # 50% of the time, we return Node 2
            return "node_2"
        # 50% of the time, we return Node 3
        return "node_3"
    ```

### Types of edges

1. **Normal Edges**: Go directly from one node to the next.
2. **Conditional Edges**: Call a function to determine which node(s) to go to next.
3. **Entry Point**: Which node to call first when user input arrives.
4. **Conditional Entry Point**: Call a function to determine which node(s) to call first when user input arrives.
