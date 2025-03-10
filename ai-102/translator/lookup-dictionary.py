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


path = '/dictionary/lookup'
constructed_url = endpoint + path

params = {
    'api-version': '3.0',
    'from': 'en',
    'to': 'pt'
}

headers = {
    'Ocp-Apim-Subscription-Key': resource_key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': region,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.
body = [{
    'text': 'beauty'
}]
request = requests.post(constructed_url, params=params, headers=headers, json=body)
response = request.json()

print(json.dumps(response, sort_keys=True, ensure_ascii=False, indent=4, separators=(',', ': ')))