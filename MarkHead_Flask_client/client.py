import requests

picture="omar_sy.png"

url = 'http://127.0.0.1:5000/analyse'
files = {'media': open(picture, 'rb')}
response = requests.post(url, files=files)
print(response.json())