# 🧠 Rudimentary CLI Chatbot

A session-based, file-persistent CLI chatbot built in Python.

This project started as a simple conversational bot and evolved into a structured, stateful system with session management and configurable memory behavior — laying the foundation for future LLM and vector database integration.

---

## 🚀 Features

- 💬 Interactive CLI chat loop
- 🗂️ Session-based conversation storage
- 💾 Persistent JSON memory per session
- 📜 `/history` – View full session history
- 🔎 `/latest` – View last N conversation pairs
- 📁 `/sessions` – List previous sessions
- ▶ `/resume <n>` – Resume a previous session
- 🧹 `/clear` – Clear current session history
- ⚙ Config-driven behavior

---

## 📁 Project Structure

```text
.
├── Rudimentary_chatbot.py   # Entry point (chat loop + routing)
├── utils.py                 # Reply generation logic
├── memory.py                # Session memory + persistence
├── config.py                # Application configuration
├── chats/                   # Session JSON files
└── README.md
```

---

## 🏗 Architecture Overview

### 1️⃣ Session-Based Storage

Each chat session is stored as:

```text
chats/session_YYYYMMDD_HHMMSS.json
```

Sessions are automatically created when the program starts.

---

### 2️⃣ Memory Format

Messages are stored as structured dictionaries:

```json
[
  { "role": "user", "content": "Hello" },
  { "role": "ai", "content": "I heard you say Hello" }
]
```

---

### 3️⃣ Command System

| Command       | Description                                                                        |
|---------------|------------------------------------------------------------------------------------|
| `/exit`       | Exit chat                                                                          |
| `/history`    | Show full session history                                                          |
| `/latest`     | Show last N exchange pairs                                                         |
| `/sessions`   | List previous sessions                                                             |
| `/resume <n>` | Resume selected session works. Only when `/sessions` command has already been used |
| `/clear`      | Clear current session                                                              |

---

## ⚙ Configuration (`config.py`)

All key behavior is configurable:

```python
MODEL_NAME = "Mock_Model"
MAX_HISTORY = 20
DEBUG_MODE = True
REVERSE_MODE = False
LATEST_EXCHANGE_PAIRS = 3
```

### Explanation

- `MAX_HISTORY` → Maximum messages stored in memory
- `LATEST_EXCHANGE_PAIRS` → Number of user/AI exchange pairs shown in `/latest`
- `DEBUG_MODE` → Prints debug logs
- `REVERSE_MODE` → Experimental reverse reply mode

---

## 🔎 How `/latest` Works

Unlike `/history`, which shows everything, `/latest`:

- Extracts complete **user → AI exchange pairs**
- Returns the last `LATEST_EXCHANGE_PAIRS`
- Ensures pairs are logically grouped

This design prepares the system for:

- Context window trimming
- LLM token management
- Prompt construction

---

## 🧠 State Management

The CLI includes a controlled resume flow:

- `/sessions` enables session selection mode
- `/resume` works only after `/sessions` is called
- This prevents invalid session selection

This introduces basic CLI state machine behavior.

---

## 🎯 Why This Project Matters

This is not just a toy chatbot.

It establishes:

- Persistent session management
- Clean message structure
- Config-driven architecture
- CLI command routing
- Memory abstraction layer

Which makes it ready for:

- LLM API integration
- Vector database storage
- FastAPI backend conversion
- Multi-user expansion

---

## 🛣 Roadmap

### Next Steps

- 🔌 Integrate OpenAI / Anthropic / Google LLM APIs
- 🧮 Add embedding generation
- 🗄 Integrate a vector database (FAISS / Milvus / Pinecone)
- 🌐 Convert to FastAPI backend
- 🖥 Build minimal web UI

---

## 🏁 Running the Project

```bash
python Rudimentary_chatbot.py
```

Sessions will automatically be created inside the `chats/` directory.

---
