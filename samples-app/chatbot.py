#!/usr/bin/env python
"""Simple CLI chatbot using the Strands SDK with OpenAI."""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Allow running without installing the package
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from strands import Agent
from strands.models import OpenAIModel


def main() -> None:
    """Run a simple CLI chatbot using OpenAI."""

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")

    model_id = os.getenv("OPENAI_MODEL_ID", "gpt-3.5-turbo")
    model = OpenAIModel(model_id=model_id, client_args={"api_key": api_key})
    agent = Agent(model=model)

    print("Strands CLI Chatbot (OpenAI)")
    print(f"Using model: {model_id}\n")
    print("Type 'exit' or press Ctrl-D to quit.\n")

    while True:
        try:
            user_input = input("You: ")
        except EOFError:
            print()
            break

        if user_input.strip().lower() in {"exit", "quit"}:
            break

        result = agent(user_input)
        print(f"Agent: {str(result).strip()}")


if __name__ == "__main__":
    main()
