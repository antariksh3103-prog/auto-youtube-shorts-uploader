import os
from openai import OpenAI
from gtts import gTTS

SCRIPT_PATH = "output/script.txt"
AUDIO_PATH = "output/voice.mp3"

def generate_voice():
    if not os.path.exists(SCRIPT_PATH):
        raise FileNotFoundError("Script not found! Run generate_script.py first.")

    with open(SCRIPT_PATH, "r", encoding="utf-8") as f:
        text = f.read()

    # Using Google Text-to-Speech as free solution
    tts = gTTS(text=text, lang="en", slow=False)
    tts.save(AUDIO_PATH)

    print("Voice generated:", AUDIO_PATH)
    return AUDIO_PATH

if __name__ == "__main__":
    generate_voice()
