## 🧠 What It Does

This project is a voice-enabled chatbot with file Q&A. It allows you to:

- 🎙️ Speak to an AI assistant (via microphone)
- 📄 Upload a PDF and ask questions based on its content
- 💬 Get intelligent, contextual answers using **Ollama** (open-source LLMs)

## 📦 Folder Structure

- `app.py`: Main Streamlit interface
- `chat_backend.py`: Handles LLM responses via Ollama
- `pdf_utils.py`: Extracts text from uploaded PDFs
- `voice_utils.py`: Records, transcribes (via Whisper), and speaks back the response
