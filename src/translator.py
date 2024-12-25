# filepath: /c:/ZONE/__PROJECT__/__PYTHON__/RealTimeTranslate/src/translator.py
from googletrans import Translator as GoogleTranslator
from gtts import gTTS
import os

class Translator:
    def __init__(self, source_lang, target_lang):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = GoogleTranslator()

    def translate_text(self, text):
        translation = self.translator.translate(text, src=self.source_lang, dest=self.target_lang)
        return translation.text

    def text_to_speech(self, text, lang):
        tts = gTTS(text=text, lang=lang)
        tts.save("translated_audio.mp3")
        os.system("start translated_audio.mp3")  # For Windows