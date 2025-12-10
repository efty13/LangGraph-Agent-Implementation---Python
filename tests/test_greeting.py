# tests/test_greeting.py

import sys
import pathlib

# Ensure project root is on sys.path so `import Prava` works
ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Prava import build_app


def test_greeting_with_name():
    app = build_app()

    result = app.invoke({"name": "Alice"})

    assert result["greeting"] == "Hello, Alice! Welcome!"
    assert result["name"] == "Alice"


def test_greeting_default_name():
    app = build_app()

    result = app.invoke({})

    assert "Guest" in result["greeting"]