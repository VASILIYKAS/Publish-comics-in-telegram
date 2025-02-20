import requests


def dowload_comics(url, file_name):

    response = requests.get(url)
    response.raise_for_status()

    with open(file_name, 'wb') as file:
        file.write(response.content)