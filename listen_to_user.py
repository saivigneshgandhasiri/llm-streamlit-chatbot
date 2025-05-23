import speech_recognition as sr
import streamlit as st

def listen_to_user(retry_on_fail=True):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            st.info("🎤 Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=2)

            st.info("🎧 Listening... Speak now.")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)

            # Save raw audio for debugging or playback
            with open("output.wav", "wb") as f:
                f.write(audio.get_wav_data())
    except Exception as mic_error:
        st.error(f"🎙️ Microphone error: {mic_error}")
        return ""

    try:
        user_text = recognizer.recognize_google(audio)
        return user_text
    except sr.UnknownValueError:
        st.warning("🤔 Sorry, I couldn't understand what you said.")
        if retry_on_fail:
            st.info("🔁 Trying again... please speak clearly.")
            return listen_to_user(retry_on_fail=False)
        return ""
    except sr.RequestError as e:
        st.error(f"❌ Network error with voice recognition: {e}")
        return ""
