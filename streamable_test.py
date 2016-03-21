import requests
import json

def upload_file(path):
    url = "https://api.streamable.com/upload"
    with open(path, 'rb') as f:
        files = {'file': f}
        r = requests.post(url, files = files)
        return json.loads(r.text)
