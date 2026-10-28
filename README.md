# claude-sandbox

My playground for learning the Claude API: first calls, prompt experiments and exercises from the Claude Academy *Building with the Claude API* course.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install anthropic python-dotenv
```

Create a `.env` file in the project folder with your key (it's git-ignored and never committed):

```
ANTHROPIC_API_KEY=your-key-here
```

## Run

```bash
python hello_claude.py
```

Sends one message to Claude and prints the reply and token usage.

## Contents

| File | What it does |
| --- | --- |
| `hello_claude.py` | First Messages API call with a system prompt |

More exercises are added as I work through the course.
