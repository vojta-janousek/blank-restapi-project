import requests
import json
import os

ENDPOINT = "http://127.0.0.1:8000/api/status/"

# cwd - current working directory
image_path = os.path.join(os.getcwd(), "contact.png")

def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)

    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, files=file_data)
    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do_img(method="post", data={'user': 2, "summary": "no summary"}, is_json=False, img_path=image_path)

do_img(
    method="put",
    data={'id': 4, 'user': 2, "summary": "updejtyd"}, 
    is_json=False,
    img_path=image_path
    )


# do(data={'id': 10})
# do(method='put', data={'id': 7, "user": 2, "summary": "updated via script"})
# do(method='delete', data={'id': 110})
# do(method='post', data={"summary": "posted via script", "user": 2})
