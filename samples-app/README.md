# Samples App

This directory contains a minimal command line chatbot using the
[Strands Agents](https://github.com/strands-agents/sdk-python) SDK with
OpenAI.

```bash
# Install the SDK with the OpenAI extra
pip install -e .[openai]
```

Set your OpenAI API key in the `OPENAI_API_KEY` environment variable and run the chatbot:

Optionally set `OPENAI_MODEL_ID` to choose a different model (defaults to `gpt-3.5-turbo`).

```bash
export OPENAI_API_KEY="sk-..."
python samples-app/chatbot.py
```

Use `CTRL-D` or type `exit` to quit the session.
