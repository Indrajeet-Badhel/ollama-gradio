import gradio as gr
import requests

# Function to chat with Ollama
def chat_with_ollama(message, history):
    if history is None:
        history = []

    # Add user message to history
    history.append({"role": "user", "content": message})

    # Call Ollama API
    response = requests.post(
        "http://localhost:11434/api/chat",
        json={
            "model": "llama3",  # ✅ Use the model you have
            "messages": history,
            "stream": False
        }
    )

    # Get assistant's reply
    reply = response.json()["message"]["content"]

    # Add assistant reply to history
    history.append({"role": "assistant", "content": reply})

    # ✅ Return only the updated history (not a tuple)
    return history

# Gradio wrapper
def gradio_chat(user_input, history=None):
    return chat_with_ollama(user_input, history)

# Gradio interface
chat_ui = gr.ChatInterface(
    fn=gradio_chat,
    title="Ollama + Gradio Chatbot",
    theme="default",
    type="messages"  # ✅ Must match your return format
)

if __name__ == "__main__":
    chat_ui.launch()
