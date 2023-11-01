import requests, uuid, json
import os
from speech import Transcribe
from dotenv import load_dotenv
load_dotenv()

# Add your key and endpoint
key = os.getenv('TRANSLATOR_KEY')
endpoint = "https://api.cognitive.microsofttranslator.com"

# location, also known as region.
# required if you're using a multi-service or regional (not global) resource. It can be found in the Azure portal on the Keys and Endpoint page.
location = "eastus"

path = '/translate'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': ['yo', 'ig','ha']
}
def translate(language, text):
    headers = {
        'Ocp-Apim-Subscription-Key': key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    # print(response)
    # print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))
    # print(response[0]['translations'][0])
    # print(response[0]['translations'][1])
    # print(response[0]['translations'][2])

    if language=='yo':
        return response[0]['translations'][0]['text']
    elif language=='ig':
        return response[0]['translations'][1]['text']
    elif language=='ha':
        return response[0]['translations'][2]['text']
    else:
        return "Wrong Language"