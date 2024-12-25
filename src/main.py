import speech_recognition as sr
from translator import Translator

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def main():
    source_lang = input("Enter the source language (e.g., 'en' for English): ")
    target_lang = input("Enter the target language (e.g., 'es' for Spanish): ")

    translator = Translator(source_lang, target_lang)

    while True:
        print("Say something to translate (or 'exit' to quit):")
        text_to_translate = recognize_speech()
        if text_to_translate and text_to_translate.lower() == 'exit':
            print("Exiting the translation app. Goodbye!")
            break

        if text_to_translate:
            translated_text = translator.translate_text(text_to_translate)
            print(f"Translated text: {translated_text}")
            translator.text_to_speech(translated_text, target_lang)

            continue_prompt = input("Do you want to translate another phrase? (yes to continue, no to stop): ").strip().lower()
            if continue_prompt != 'yes':
                print("Exiting the translation app. Goodbye!")
                break

if __name__ == "__main__":
    main()