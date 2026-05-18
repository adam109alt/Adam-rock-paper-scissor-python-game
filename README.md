# 🤖 DevAssistant — AI-Powered PC Agent

> Control your computer with plain English. DevAssistant is a terminal-based AI agent that runs commands, creates files, searches the web, and generates code — all from a single conversation.

---

## 🧠 How It Works

DevAssistant uses **Google Gemini 2.5 Flash** as its brain. You talk to it in natural language, and it decides which tool to use to get the job done. It can chain tools together — for example, search the web for an idea, then use that idea to generate and save a file.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🖥️ **CMD Execution** | Runs system commands directly on your machine |
| 📁 **File Creation** | Creates and writes files with AI-generated content |
| 🌐 **Web Search** | Uses Tavily for real-time search when the AI needs current info |
| 👨‍💻 **Code Generation** | Delegates complex coding tasks to Mistral's Devstral model |
| 📖 **File Reading** | Reads any local file by its path |
| 💾 **Session Memory** | Save and load full conversation history as JSON |

---

## 🛠️ Tech Stack

- **[Google Gemini 2.5 Flash](https://ai.google.dev/)** — Main AI brain (reasoning + tool use)
- **[Mistral Devstral](https://mistral.ai/)** — Specialized code generation model
- **[Tavily](https://tavily.com/)** — Real-time web search API
- **[Rich](https://github.com/Textualize/rich)** — Beautiful terminal output with Markdown rendering

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/devassistant.git
cd devassistant
```

### 2. Install dependencies

```bash
pip install google-genai mistralai tavily-python python-dotenv rich
```

### 3. Set up your API keys

Create a file called `api.env` in the project root:

```env
GEMINI_API_KEY=your_gemini_key_here
TAVILY_API_KEY=your_tavily_key_here
MISTRAL_API_KEY=your_mistral_key_here
```

---

## 🚀 Usage

```bash
python main.py
```

Then just type what you want:

```
> What Python version do I have?
> Create a file called notes.txt with 5 productivity tips
> Search for the latest FastAPI features and write a summary file
> Fix the error in my script.py
```

### Special Commands

| Command | What it does |
|---|---|
| `save` | Saves the current conversation to a `.json` file |
| `load` | Loads a previously saved conversation |
| `exit` | Exits the program |

---

## 💡 Example Use Cases

- **"What files are in my Downloads folder?"** → Runs a CMD command and shows the result
- **"Make a Python script that renames all .jpg files in this folder"** → Generates the code using Mistral, saves the file
- **"Search for the best way to use async in Python and save a summary"** → Web search + file creation
- **"Read my config.json and explain what it does"** → File reading + AI explanation

---

## 📁 Project Structure

```
devassistant/
│
├── main.py          # Entry point — the main agent loop
├── api.env          # Your API keys (not committed to git)
└── README.md
```

---

## ⚠️ Important Notes

- This agent **runs real commands** on your machine. Use it carefully.
- Make sure your `api.env` file is in your `.gitignore` so you never upload your API keys.
- The Mistral coding tool has its own memory within a session, so you can have multi-turn coding conversations.

---

## 🔒 .gitignore Recommendation

```
api.env
*.json
__pycache__/
```

---

## 📄 License

MIT License — feel free to use, modify, and build on this project.

---

Made with ❤️ using Gemini, Mistral, and Tavily.
