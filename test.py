import requests, json

BASE_URL = "http://127.0.0.1:8090"
ENDPOINT = "/1"
headers = {'Content-Type': 'application/json'}
data = {"name": 'gagnam style', "views": 10}

response = requests.put(BASE_URL + ENDPOINT, data=json.dumps(data), headers=headers)
print(response.json())
