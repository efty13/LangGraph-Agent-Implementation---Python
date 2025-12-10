from langgraph.graph import StateGraph


# ---------- State Schema ----------
class State(dict):
    """
    Graph state with input 'name' and output 'greeting'.
    """
    name: str
    greeting: str


# ---------- Node Function ----------
def greeting_node(state: State):
    # Read input name from state
    name = state.get("name", "Guest")
    greeting = f"Hello, {name}! Welcome!"

    # Debug prints so we see what's happening
    print("[greeting_node] input state:", state)
    print("[greeting_node] output state:", {"greeting": greeting})

    # Return updated part of the state
    return {"greeting": greeting}


# ---------- Build Graph ----------
def build_app():
    graph = StateGraph(State)

    # Add single node
    graph.add_node("greet", greeting_node)

    # START -> greet -> END
    graph.add_edge("__start__", "greet")
    graph.add_edge("greet", "__end__")

    # Compile the graph into an app
    return graph.compile()


# ---------- Entry Point ----------
if __name__ == "__main__":
    print("[main] building app...")
    app = build_app()

    print("[main] invoking graph...")
    result = app.invoke({"name": "Eftal"})

    print("[main] final result:", result)