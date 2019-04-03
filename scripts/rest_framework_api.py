import requests
import json

ENDPOINT = "http://127.0.0.1:8000/api/status/"

def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do(data={'id': 10})
# do(method='put', data={'id': 7, "user": 2, "summary": "updated via script"})
# do(method='delete', data={'id': 110})
# do(method='post', data={"summary": "posted via script", "user": 2})
