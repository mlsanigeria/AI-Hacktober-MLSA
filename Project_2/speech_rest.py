import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

# Azure Speech Service API credentials
subscription_key =  os.getenv('COG_SERVICE_KEY')
service_region = os.getenv('COG_SERVICE_REGION')  # e.g., 'eastus'
def Transcribe(filename):
    # Audio file to transcribe
    # audio_file = 'audio.wav'

    # Set up the API endpoint
    base_url = f'https://{service_region}.api.cognitive.microsoft.com/sts/v1.0/issueToken'
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    token = requests.post(base_url, headers=headers).text

    headers = {
        'Authorization': f'Bearer {token}',
    }

    # Prepare and send the audio data for transcription
    with open(filename, 'rb') as audio_file:
        base_url = f'https://{service_region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1'
        query_parameters = {
            'language': 'en-US',  # Change this to your audio language code
        }

        response = requests.post(base_url, params=query_parameters, headers=headers, data=audio_file)

    # Check the response status and wait for the transcription to complete
    if response.status_code == 202:
        response_data = response.json()
        transcription_url = response_data['recognitionStatus']

        while transcription_url == 'Running':
            time.sleep(5)
            response = requests.get(response.headers['location'], headers=headers)
            response_data = response.json()
            transcription_url = response_data['recognitionStatus']

        if transcription_url == 'Succeeded':
            transcription_text = response_data['DisplayText']
            # print('Transcription:')
            # print(transcription_text)
            output = transcription_text
        else:
            output = 'Transcription failed.'
    else:
        try:
            output = response.json()['DisplayText']
        except:
            output  = 'Transcription failed.'
        # print(f'Request failed with status code {response.status_code}: {response.text.DisplayText}')
    return output
