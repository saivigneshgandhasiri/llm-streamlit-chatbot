import streamlit as st
from chat_backend import get_ollama_response
from pdf_utils import extract_text_from_pdf
from voice_utils import listen_to_user, speak_response

st.set_page_config(page_title="AI Voice Chatbot", layout="wide")
st.title("🎤 Voice Chatbot with File Q&A")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
pdf_text = extract_text_from_pdf(uploaded_file) if uploaded_file else ""

# Session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Chat display
for role, msg in st.session_state['chat_history']:
    st.chat_message(role).write(msg)

# Text Input
user_input = st.chat_input("Type your message...")
if user_input:
    st.session_state['chat_history'].append(("user", user_input))
    response = get_ollama_response(user_input, pdf_text)
    st.session_state['chat_history'].append(("bot", response))

# Voice Input
if st.button("🎤 Start Voice Chat"):
    with st.spinner("Listening... Please speak into your mic."):
        from voice_utils import listen_to_user_with_whisper
        voice_input = listen_to_user_with_whisper()

    
    st.text_area("You said:", voice_input)

    if voice_input and not voice_input.startswith("❌") and not voice_input.startswith("⏰") and not voice_input.startswith("🌐"):
        st.session_state['chat_history'].append(("user", voice_input))
        context = pdf_text
        response = get_ollama_response(voice_input, context)
        st.session_state['chat_history'].append(("bot", response))
        speak_response(response)
        st.text_area("Bot Response", response)

