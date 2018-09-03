import json
from urllib import request
from urllib.request import urlopen

# Address for sending JSON requests
from flask import app, Flask

app = Flask(__name__)

url = 'https://api.weather.yandex.ru/v1/informers?lat=55.75396&lon=37.620393'

# data for OAuth authorization
token = 'e4d3b4d2a7444fa384a18cda5cd1c8d9'

# Yandex.Direct login
login = 'agrom'
# X-Yandex-API-Key
# input data structure (dictionary)
data = {
   'method': 'GetClientInfo',
   'token': token,
   'locale': 'ru',
   'param': [login]
}


@app.route('/')
def index():
    req = request.Request(url, headers={"X-Yandex-API-Key" : "02d3e606-cc1e-4c83-a3a5-55add3fa5f1b"})
    with request.urlopen(req) as response:
        print(response.read().decode('utf8'))

    # output the result
    return 'Index Page'


