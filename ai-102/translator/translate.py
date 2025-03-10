import os, requests, uuid, json
from dotenv import load_dotenv

load_dotenv()

key_var_name = 'TRANSLATOR_TEXT_RESOURCE_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
resource_key = os.environ[key_var_name]

region_var_name = 'TRANSLATOR_TEXT_REGION'
if not region_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(region_var_name))
region = os.environ[region_var_name]

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

path = '/translate'
params = {
    'api-version': '3.0',
    # don't provide the below line if you want auto language detection
    # 'from': 'en', 
    'to': ['sw', 'it'],
    # get original and translated sentence length
    'includeSentenceLength': True

}
constructed_url = endpoint + path

headers = {
    'Ocp-Apim-Subscription-Key': resource_key,
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text' : 'Hello World!'
}]

request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()
print(json.dumps(body))
print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))