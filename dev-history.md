# 📘  dev-history.md

Project: LangGraph Single-Node Greeting Agent (Python)

This document captures the complete development process, decisions, challenges, and prompts used while implementing the LangGraph agent for the internship task.

⸻

# 1. Initial Understanding of the Task

After reading the task PDF, the main requirements were:
-	Create a single-node LangGraph agent
-	The node should accept a name as input
-	It should return a greeting string as output
-	Graph structure must follow:
START → greeting_node → END
-	No LLMs allowed
-	Use uv for environment and dependency management
-	Publish as a clean GitHub repository
-	Include documentation + dev-history
-	Bonus: include a unit test and (optional) MCP configuration

I clarified the architecture before coding to avoid unnecessary redesign later.

⸻

# 2. Setting Up the Environment

## Steps Taken
-	Installed uv using the official script.
-	Created an isolated project environment with uv sync.
-	Installed only what was necessary for the final agent:
```bash
langgraph
pytest
```

Why not include langchain / anthropic?

Initially I experimented with langchain[anthropic] because it was installed by default in a previous environment.
This caused:
- Import conflicts
- Pytest misbehaving
- ModuleNotFoundError: Prava during test discovery
- SSL warnings from urllib3 due to macOS LibreSSL

Decision: Remove all unnecessary dependencies and keep the environment minimal.

⸻

# 3. Implementing the First Version of the Agent

The first Python file I tested was not aligned with the PDF.
It used:
```bash
MessagesState
mock_llm()
graph.invoke(...)
```

This ran silently because nothing was printed.
It also violated the rules:
- Used LLM messaging structure
- Lacked a name→greeting transformation
- Lacked START→END structure
- No clean state schema

Decision: Rewrite the entire file into a clean LangGraph implementation.

⸻

## 4. Final Agent Implementation

Created Prava.py with:

✔️ State schema
```bash
class State(dict):
    name: str
    greeting: str
```

✔️ Node
```bash
def greeting_node(state):
    name = state.get("name", "Guest")
    return {"greeting": f"Hello, {name}! Welcome!"}
```

✔️ Graph structure
```bash
graph.add_node("greet", greeting_node)
graph.add_edge("__start__", "greet")
graph.add_edge("greet", "__end__")
```
✔️ Invocation
```bash
app.invoke({"name": "Eftal"})
```
Added debug prints to verify graph execution during early testing.

# 5. Writing Unit Tests

Created tests/test_greeting.py including two cases:
	1.	Greeting with a provided name
	2.	Greeting with default name (Guest)

Used direct assert checks to validate correctness.

All tests passed after import path fix.

# 6. Interactions with AI Assistant

Throughout development I used ChatGPT and ClaudeAI to:
- Clarify LangGraph API usage
- Debug import issues
- Validate correct graph structure
- Improve README formatting
- Generate examples of unit tests
- Explain SSL/LibreSSL warnings on macOS
