from azure.ai.translation.text import *
from azure.ai.translation.text.models import InputTextItem
from dotenv import load_dotenv
import os

def main():
    try:
        load_dotenv()
        translator_endpoint = os.getenv('TRANSLATOR_TEXT_ENDPOINT')
        translator_key = os.getenv('TRANSLATOR_TEXT_RESOURCE_KEY')
        translator_region = os.getenv('TRANSLATOR_TEXT_REGION')

        credential = TranslatorCredential(translator_key, translator_region)
        client = TextTranslationClient(credential)

        # choose target language 

        languageResponse = client.get_languages(scope="translation")
        print("{} language supported.". format(len(languageResponse.translation)))
        print("(See https://learn.microsoft.com/azure/ai-services/translator/language-support#translation)")
        print("Enter a target language code for translation(for example, 'en'): ")

        targetLanguage = "xx"
        supportedLanguage = False

        while supportedLanguage == False:
            targetLanguage = input()
            if targetLanguage in languageResponse.translation.keys():
                supportedLanguage = True
            else:
                print("{} is not supported language.". format(targetLanguage))

        inputText = ""

        while inputText.lower() != "quit":
            inputText = input("Enter text to translate('quit' to exit):")
            if inputText != "quit":
                input_text_elements = [InputTextItem(text=inputText)]
                translationResponse = client.translate(content=input_text_elements, to=[targetLanguage])
                translation = translationResponse[0] if translationResponse else None
                if translation:
                    sourceLanguage = translation.detected_language
                    for translated_text in translation.translations:
                        print(f"'{inputText}' was translated from {sourceLanguage.language} to {translated_text.to}")
                        print(f"'{inputText}' was translated to {translated_text.text}")
    
    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()