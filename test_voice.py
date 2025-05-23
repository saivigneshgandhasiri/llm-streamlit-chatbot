import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Testing mic... Speak now.")
    r.adjust_for_ambient_noise(source, duration=2)
    audio = r.listen(source, timeout=15, phrase_time_limit=30)

with open("mic_test.wav", "wb") as f:
    f.write(audio.get_wav_data())

print("🎧 Audio saved to mic_test.wav")
