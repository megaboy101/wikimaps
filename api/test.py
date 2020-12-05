import requests

BASE = 'http://127.0.0.1:5000/'

# Un-comment and edit either request below to test functionality of api.py

response = requests.get(BASE + 'path', {'src-id': 316, 'dest-id': 54})
#response = requests.get(BASE + 'title', {'title': "Albert Einstein"})
print(response.json()) 