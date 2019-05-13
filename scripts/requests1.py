import requests


def main():
    response = requests.get("http://www.google.com")
    print("Status code: ", response.status_code)
    print("Headers/Content-Type: ", response.headers['Content-Type'])


if __name__ == '__main__':
    main()
