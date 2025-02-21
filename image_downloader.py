import requests


def dowload_comics(url, comics_title):
    response = requests.get(url)
    response.raise_for_status()

    with open(comics_title, 'wb') as file:
        file.write(response.content)