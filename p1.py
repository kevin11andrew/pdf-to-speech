import fitz
from gtts import gTTS
import pyttsx3
import os

engine = pyttsx3.init()
doc=fitz.open("filename.pdf")
for page in doc:
    text=page.get_text()
    engine.say(text)
    engine.runAndWait()