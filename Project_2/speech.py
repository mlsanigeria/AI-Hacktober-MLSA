import os
from dotenv import load_dotenv
from datetime import datetime
#import namespaces
import azure.cognitiveservices.speech as speech_sdk

#get configuration settings
load_dotenv()
cog_key = os.getenv('COG_SERVICE_KEY')
cog_region = os.getenv('COG_SERVICE_REGION')

#configure speech service
speech_config = speech_sdk.SpeechConfig(cog_key, cog_region)
#print('Ready to use speech service in:', speech_config.region)

def Transcribe(filename):
    command = ''

    #configure speech recognition
    audio_config = speech_sdk.AudioConfig(filename=filename)
    #audio_config = speech_sdk.AudioConfig(use_default_microphone = True)
    
    #process speech input
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        #print(command)
    else:

        # print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    return command
