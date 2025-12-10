# 📘 LangGraph Python Agent – Single-Node Greeting Graph

This repository contains a minimal yet complete LangGraph agent, implemented in Python using uv as the package and environment manager.
The goal of this project is to demonstrate the ability to:
- Work with a novel framework (LangGraph)
- Understand graph-based agent architecture
- Implement a non-LLM computation node
-	Manage Python project dependencies via uv
- Design, test, and document software cleanly

This project is built according to the full specifications outlined in the internship technical assignment.

⸻

# 🧭 Overview

The agent is intentionally simple:
- It accepts a name as input
- It returns a greeting message as output
- It uses one computation node
-	It follows a strict graph structure:
START → greet → END
-	No language model (LLM) is used at any stage
-	The implementation is fully deterministic and minimal

This repository also includes:
- A detailed development history (dev-history.md)
- A minimal test suite (pytest)
-	Clean dependency management (uv)
-	A structured and readable project layout

⸻

# 🗂️ Project Structure

```code
.
├── Prava.py                      # Main LangGraph agent implementation
├── README.md                     # Documentation
├── dev-history.md                # Development log as required by assignment
├── pyproject.toml                # Project metadata + dependencies
├── uv.lock                       # uv dependency lock file
└── tests/
    └── test_greeting.py          # Unit tests for the greeting agent
```

# ⚙️ Technologies & Tools Used

Tool                Purpose
Python 3.9+         Primary programming language
uv                  Environment & dependency manager (required by task)
LangGraph           Framework for building stateful agent 
Pytest              Unit testing framework
macOS terminal      Runtime environment

# 🚀 Getting Started

## 1. Install uv

If you don’t already have it installed:

macOS / Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows PowerShell:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```
## 2. Install project dependencies

Inside the project directory:
```bash
uv sync
```
This will:
- Create the virtual environment (.venv)
- Install all dependencies from pyproject.toml
- Generate or update uv.lock

## 3. Run the agent
```bash
uv run Prava.py
```
You should see output similar to:
```code
[main] building app...
[main] invoking graph...
[greeting_node] input state: {'name': 'Eftal'}
[greeting_node] output state: {'greeting': 'Hello, Eftal! Welcome!'}
[main] final result: {'name': 'Eftal', 'greeting': 'Hello, Eftal! Welcome!'}
```

# 🧩 How the Agent Works

LangGraph represents computation as a stateful directed graph.
In this project:

## ✔️ State Schema

The agent attaches two fields to its state:
```python
class State(dict):
    name: str
    greeting: str
```
## ✔️ Node Function

A single node transforms the input state:
```python
def greeting_node(state):
    name = state.get("name", "Guest")
    return {"greeting": f"Hello, {name}! Welcome!"}
```
## ✔️ Graph Structure

The specification requires:
```code
START → greet → END
```

This is implemented using:
```python
graph.add_edge("__start__", "greet")
graph.add_edge("greet", "__end__")
```

## ✔️ Invocation

The graph is compiled into an executable:

```python
app = graph.compile()
app.invoke({"name": "Eftal"})
```
## 🔍 Complete Flow Diagram

Below is a conceptual overview of how data flows through this agent:

```code
┌────────────┐
│   START     │
└──────┬──────┘
       │
       ▼
┌────────────┐
│  greet()    │
│ - read name │
│ - build msg │
└──────┬──────┘
       │
       ▼
┌────────────┐
│    END      │
└────────────┘
```

## 🧪 Running Unit Tests

To validate the behavior of the agent:

```bash
uv run pytest
```

The test suite covers:
	1.	Greeting with a supplied name
	2.	Greeting using the default "Guest" behavior

Expected output:

```code
tests/test_greeting.py ..                                          [100%]
```

## 🛠️ File: Prava.py

The full implementation looks like this:

```python
from langgraph.graph import StateGraph

class State(dict):
    name: str
    greeting: str

def greeting_node(state: State):
    name = state.get("name", "Guest")
    greeting = f"Hello, {name}! Welcome!"
    print("[greeting_node] input state:", state)
    print("[greeting_node] output state:", {"greeting": greeting})
    return {"greeting": greeting}

def build_app():
    graph = StateGraph(State)
    graph.add_node("greet", greeting_node)
    graph.add_edge("__start__", "greet")
    graph.add_edge("greet", "__end__")
    return graph.compile()

if __name__ == "__main__":
    print("[main] building app...")
    app = build_app()
    print("[main] invoking graph...")
    result = app.invoke({"name": "Eftal"})
    print("[main] final result:", result)
```

## 📚 Development History

A full narrative of the development process, mistakes, debugging sessions, design decisions, and prompt usage is documented in:

## 👉 dev-history.md

This file is required by the assignment and has been completed in detail.

⸻

## 🧹 Code Quality & Principles Followed

Throughout the development:
- Minimal dependencies were maintained
- No unused imports or LLM integrations
- State flow is explicit and predictable
- The project remains easy to extend

Future improvements could include:
-	Adding CLI input
-	Extending the graph with additional nodes
- Implementing LangSmith visualization
- Adding MCP integration for IDE tooling

⸻

## 📜 License

This project is released under the MIT License.

⸻

## 🙌 Final Notes

This repository is intentionally simple, but it demonstrates:
- Ability to read and understand new documentation quickly
-	Ability to build correct graph structures
-	Ability to debug Python import and dependency issues
-	Ability to write clean, maintainable code
-	Ability to document the development process professionally







