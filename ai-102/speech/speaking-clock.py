from datetime import datetime
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound
from dotenv import load_dotenv
import os


def TranscribeCommand():
    command = ''

    # configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)

    print("What is the speech service you want to use?")
    print("1. Use audio input from a file")
    print("2. Use microphone input")
    
    while True:
        choice = input("Please select 1 or 2: ")
        
        choice = int(choice)
        
        if choice == 1:
            print("You selected audio input from a file")
            current_dir = os.getcwd()
            audioFile = os.path.join(current_dir, 'ai-102\speech\\time.wav')

            if not os.path.exists(audioFile):
                raise FileNotFoundError(f"Audio file not found at {audioFile}")

            audio_config = speech_sdk.AudioConfig(filename=audioFile)
            speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
            print("Speak now...")
            playsound(audioFile)

            break
        elif choice == 2:
            print("You selected microphone input")
            speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
            print("Speak now...")
            
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")
    

    # process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-LibbyNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Use Speech Synthesis Markup Language
    # responseSsml = " \
    #     <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
    #         <voice name='en-GB-LibbyNeural'> \
    #             {} \
    #             <break strength='weak'/> \
    #             Time to end this lab! \
    #         </voice> \
    #     </speak>".format(response_text)
    # speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
    # if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
    #     print(speak.reason)


    # Print the response
    print(response_text)
    

def main():
    try:
        load_dotenv()
        ai_key = os.getenv("SPEECH_KEY")
        ai_region = os.getenv("SPEECH_REGION")

        global speech_config

        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print("Ready to use speech service in:", speech_config.region)


        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()
        
    except Exception as ex:
        print(ex)

if __name__ =="__main__":
    main()