import json
import requests

print('rchat test started!')

api_token = 'your_api_token'
api_url_base = 'https://rchat.blogic.ru'

headers = {
    'X-Auth-Token': 'token',
    'X-User-Id': 'user-id'
}

data = {
    'channel': '#tn.dev.stayhome',
    'text': '+'
}

api_url = '{0}/api/v1/chat.postMessage'.format(api_url_base)

response = requests.post(api_url, headers=headers, data=data)

result = None
if response.status_code >= 500:
    print('[!] [{0}] Server Error'.format(response.status_code))
elif response.status_code == 404:
    print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
elif response.status_code == 401:
    print('[!] [{0}] Authentication Failed'.format(response.status_code))
elif response.status_code == 400:
    print('[!] [{0}] Bad Request'.format(response.status_code))
elif response.status_code >= 300:
    print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
elif response.status_code == 200:
    result = json.loads(response.content.decode('utf-8'))
else:
    print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))


if result is not None:
    print("Here's your info: ")
    for k, v in result.items():
        print('{0}:{1}'.format(k, v))

else:
    print('[!] Request Failed')

print('rchat test finished!')
