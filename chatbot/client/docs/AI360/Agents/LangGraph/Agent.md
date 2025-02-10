1. In the above router, we invoked the model and, if it choose to call a tool, we returned a ToolMessage to the user.
 ![ReAct](../images/re-act.png)
2. But what if we call the model sequentially(again and again) to achieve the desired result. This is the intuition behind ReAct, a general agent architecture.
Learn More About [ReAct](https://react-lm.github.io/)

 ```python
    from langgraph.graph import START, StateGraph
    from langgraph.prebuilt import tools_condition
    from langgraph.prebuilt import ToolNode
    from IPython.display import Image, display

    # Graph
    builder = StateGraph(MessagesState)

    # Define nodes: these do the work
    builder.add_node("assistant", assistant)
    builder.add_node("tools", ToolNode(tools))

    # Define edges: these determine how the control flow moves
    builder.add_edge(START, "assistant")
    builder.add_conditional_edges(
        "assistant",
        # If the latest message (result) from assistant is a tool call -> tools_condition routes to tools
        # If the latest message (result) from assistant is a not a tool call -> tools_condition routes to END
        tools_condition,
    )
    builder.add_edge("tools", "assistant")
    react_graph = builder.compile()
    ```
 ![ReAct](../images/ReAct.jfif)

3. Here you can see, we have established new edge from "tool" to "assistant",  for calling the assistant again and again.