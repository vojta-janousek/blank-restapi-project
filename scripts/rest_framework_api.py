import requests
import json
import os


AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# cwd - current working directory
image_path = os.path.join(os.getcwd(), "contact.png")

data = {
    'username': 'vojta',
    'password': 'kobliha',
}
headers = {
    "Content-Type": "application/json",
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()['token']
print(token)

BASE_ENDPOINT = "http://127.0.0.1:8000/api/status/"
ENDPOINT = BASE_ENDPOINT + "17/"

data2 = {
    'summary': 'this new contl,l,mnjnent post',
}
headers2 = {
    #"Content-Type": "application/json",
    "Authorization": "JWT " + token,
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image,
    }
    r = requests.put(ENDPOINT, data=data2, headers=headers2, files=file_data)
    print(r.text)
    # r = requests.post(BASE_ENDPOINT, data=data2, headers=headers2, files=file_data)
    # print(r.text)

# ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
#
# # cwd - current working directory
# image_path = os.path.join(os.getcwd(), "contact.png")
#
# data = {
#     'username': 'ronald10',
#     'email': 'ronald10@email.com',
#     'password': 'ronaldkobliha',
#     'password2': 'ronaldkobliha'
# }
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywidXNlcm5hbWUiOiJyb25hbGQ5IiwiZXhwIjoxNTU1MjYxNDM0LCJlbWFpbCI6InJvbmFsZDlAZW1haWwuY29tIiwib3JpZ19pYXQiOjE1NTUyNjEwMzZ9.3-cocQMDJTV55pmGUB3MJQaoiWQCvNgBwgj_Qr4eHu0"
# }
#
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json() #['token']
# print(token)

# refresh_data = {
#     'token': token
# }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()
# print(new_token)

# get_endpoint = ENDPOINT + str(12)

# headers = {
#     # "Content-Type": "application/json",
#     "Authorization": "JWT " + token,
# }

# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     data = {
#         "summary": "very new content"
#     }
#     json_data = json.dumps(data)
#     posted_response = requests.post(ENDPOINT, data=data, headers=headers, files=file_data)
#     print(posted_response.text)
#
# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content-type': 'application/json'
# }
#
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)

# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {
#                 'image': image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
# # do_img(method="post", data={'user': 2, "summary": "no summary"}, is_json=False, img_path=image_path)
#
# do_img(
#     method="put",
#     data={'id': 4, 'user': 2, "summary": "updejtyd"},
#     is_json=False,
#     img_path=image_path
#     )


# do(data={'id': 10})
# do(method='put', data={'id': 7, "user": 2, "summary": "updated via script"})
# do(method='delete', data={'id': 110})
# do(method='post', data={"summary": "posted via script", "user": 2})
