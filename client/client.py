#!/bin/python3
import requests
import json

url = 'http://localhost:5000/uploader'
files = {'file': open('x.jpg', 'rb')}

r = requests.post(url, files=files)
result=json.loads(r.text)

print(f'Status: {result["status"]}')
print(f'filename: {result["filename"]}')
print(f'points:  {result["points"]}')