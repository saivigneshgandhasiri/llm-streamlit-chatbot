from faster_whisper import WhisperModel
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile
import pyttsx3

# GPU-enabled Whisper model (load once globally)
model = WhisperModel("base", device="cuda", compute_type="float16")

def listen_to_user(duration=5, samplerate=16000):
    print("🎙️ Recording... Speak now.")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, samplerate, audio)
        segments, _ = model.transcribe(f.name, beam_size=5)
        for segment in segments:
            return segment.text
    return ""

def speak_response(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
