# 🧠Rudimentary Chatbot

A modular command-line chatbot built in Python with clean separation of concerns and configurable behavior.

This project serves as a foundational backend architecture for future AI systems (LLM integration, RAG pipelines, agent workflows, etc.).

---

## 🚀 Features

- Interactive CLI chat loop  
- Modular architecture  
- In-memory conversation storage  
- Config-driven behavior  
- Debug logging mode  
- Reverse response mode  
- Command-based controls  
- Automatic history trimming  

---

## 📂 Project Structure

```text
.
├── Rudimentary chatbot.py   # Entry point (chat loop + command routing)
├── utils.py                 # Reply generation logic
├── memory.py                # Conversation memory management
├── config.py                # Application configuration
└── README.md
```

---

## 🏗 Architecture Overview

This Project follows a clean layered architecture

| File                     | Responsibility                        |
| ------------------------ | ------------------------------------- |
| `Rudimentary chatbot.py` | Main control loop & command handling  |
| `utils.py`               | Message processing & reply logic      |
| `memory.py`              | State management & history formatting |
| `config.py`              | Runtime configuration                 |

This design ensures:

- Clear separation of logic
- Easy scalability
- Swappable storage layer
- Easy future LLM integration

---

## ⚙️ Configuration

All runtime settings are centralized in config.py:

```python
MODEL_NAME = "Mock_Model"
MAX_HISTORY = 5
DEBUG_MODE = True
REVERSE_MODE = False
```

Config Options

- MODEL_NAME → Placeholder for future model integration
- MAX_HISTORY → Maximum stored messages
- DEBUG_MODE → Enables internal debug logging
- REVERSE_MODE → Reverses message content in responses
  
---

## 💬 Available Commands

| Command    | Description                            |
| ---------- | -------------------------------------- |
| `/exit`    | Exit the chatbot                       |
| `/history` | Display full conversation history      |
| `/latest`  | Show the latest `MAX_HISTORY` messages |
| `/clear`   | Clear conversation history             |

---

## 💾 Memory System

Conversation history is stored as a list of dictionaries:

```python
[
    {"role": "user", "content": "hello"},
    {"role": "ai", "content": "Hi there!"}
]
```

History is automatically trimmed:

```python
if len(history) > MAX_HISTORY:
    history[:] = history[-MAX_HISTORY:]
```

---

## 🛠 Reply Logic

The chatbot:

- Finds the latest user message
- Applies conditional logic
- Supports:
  - Keyword detection (Python / Java)
  - Uppercase detection
  - Lowercase detection
  - Reverse mode
  - Debug output

Designed to be easily replaced with real LLM API calls later.

---

## ▶️ How to Run

Make sure Python 3.10+ is installed.

```bash
python "Rudimentary chatbot.py"
```

Start chatting in the terminal.

---

## 🎯 Design Goals

- Practice modular backend design
- Understand state management
- Implement command routing
- Build scalable AI system foundations

---

## 🔮 Future Improvements

- File-based persistence (JSON storage)
- PostgreSQL integration
- FastAPI backend
- LLM API integration (OpenAI / Anthropic)
- Streaming responses
- RAG document ingestion
- Agent tool execution layer

---

## 📜 Licences

[MIT](https://choosealicense.com/licenses/mit/)

---

Built as part of a structured journey toward AI backend engineering and orchestration systems.

---
