1. Now, we are going to build the simple graph from our components defined above.

    ```python
    from IPython.display import Image, display
    from langgraph.graph import StateGraph, START, END

    # Build graph
    builder = StateGraph(State)
    builder.add_node("node_1", node_1)
    builder.add_node("node_2", node_2)
    builder.add_node("node_3", node_3)

    # Logic
    builder.add_edge(START, "node_1")
    builder.add_conditional_edges("node_1", decide_mood)
    builder.add_edge("node_2", END)
    builder.add_edge("node_3", END)

    # Add
    graph = builder.compile()

    # View
    display(Image(graph.get_graph().draw_mermaid_png()))
    ```

2. The StateGraph class is the graph class that we can use to used to build the graph for decision flow.

3. First, we initialize a StateGraph with the State class we defined above.

4. Then, we add our nodes and edges, We use the START Node, a special node that sends user input to the graph, to indicate where to start our graph.

5. The END Node is a special node that represents a terminal node.

6. Finally, we compile our graph to perform a few basic checks on the graph structure. We can visualize the graph as a diagram.