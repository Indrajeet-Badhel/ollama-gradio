# 🧠 Ollama + Gradio Chatbot

A private, locally-hosted AI chatbot using [Ollama](https://ollama.com/) and [Gradio](https://www.gradio.app/). No OpenAI key needed — works entirely offline after setup!

This project lets you build and interact with LLMs like `llama3` through a simple browser-based UI.

---

## 🔧 Features

- Chat with open-source LLMs like **llama3**, **mistral**, etc.
- Clean UI powered by **Gradio**
- Fully local — **no internet needed after setup**
- Lightweight and beginner-friendly Python code

---

## 🛠️ Installation

### 1. Install Python dependencies

Make sure you have Python 3.10+ installed.

```bash
pip install gradio requests
```
2. Install Ollama
Download and install Ollama from their official site:

🔗 https://ollama.com/download

Then run it to start the local model server.

🧠 Load a Model (e.g., llama3)
```bash

ollama pull llama3
```
You can also use:

```bash
ollama pull mistral
ollama pull gemma
```
🚀 Run the Chatbot
Once everything is installed:

```bash
python chatbot.py
```
Then open:
🔗 http://127.0.0.1:7860

💬 How It Works
The Gradio UI takes user input.

The message is passed to Ollama's local server via localhost:11434.

The model replies based on the full message history.

Replies are displayed back in the browser.

🧩 File Structure
```bash

📦 chatbot-usingollama-and-gradio/
├── chatbot.py       # Main chatbot logic
├── README.md        # Project documentation
```
📈 Future Features (Optional Ideas)
You can upgrade this bot by adding:

✅ Streaming responses (real-time typing effect)

🗃️ Chat history export to .txt or .json

🎙️ Voice input and text-to-speech output

🔄 Switch between models with a dropdown

📱 Mobile-optimized layout

🤖 Example Models to Try
Model	Command	Notes
LLaMA 3	ollama pull llama3	Great general-purpose LLM
Mistral	ollama pull mistral	Fast and lightweight
Gemma	ollama pull gemma	Smaller, efficient

🧑‍💻 Built By
Indrajeet Badhel
B.Tech Computer Science @ Vishwakarma Institute of Technology
Passionate about AI/ML, Robotics, and Web3

