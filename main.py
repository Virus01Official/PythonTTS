from gtts import gTTS
import os

def text_to_speech(text, lang='en'):
    speech = gTTS(text=text, lang=lang, slow=False)
    speech.save("output.mp3")
    os.system("start output.mp3")

text_to_speech('Hello, world!')
