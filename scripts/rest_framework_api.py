import requests
import json
import os


ENDPOINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

# cwd - current working directory
image_path = os.path.join(os.getcwd(), "contact.png")

data = {
    'username': 'vaclav',
    'email': 'elemer@email.com',
    'password': 'vaclavkobliha',
    'password2': 'vaclavkobliha'
}
headers = {
    "Content-Type": "application/json",
    # "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InZvanRhIiwiZXhwIjoxNTU0NjU5NDY1LCJlbWFpbCI6IiIsIm9yaWdfaWF0IjoxNTU0NjU5MTY1fQ.kQ6-oG9r6FNalds9LYjsk2kzYAyd4ibEWO8gBJ-0F0s"
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json() #['token']
print(token)

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
