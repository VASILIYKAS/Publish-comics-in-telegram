import requests
import random


RANDOM_RANGE_START = 1
NUMBER_LAST_COMICS = 3052


def get_random_comics_info():
    random_number = random.randint(RANDOM_RANGE_START, NUMBER_LAST_COMICS)
    comics_info = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(comics_info)
    response.raise_for_status()

    comics = response.json()
    comics_title = comics['title']
    comics_image_url = comics['img']

    return comics_title, comics_image_url