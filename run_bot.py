import os
from dotenv import load_dotenv
from telegram import Bot
from fetch_comics import get_random_comics_info
from image_downloader import dowload_comics
from post_telegram_bot import post_image
from image_handler import check_size, remove_comics


def main():
    load_dotenv()

    tg_token = os.environ['TG_TOKEN']
    bot = Bot(token=tg_token)
    channel_id = os.environ['TG_CHAT_ID']

    comics_title, comics_image_url, file_name = get_random_comics_info()
    dowload_comics(comics_image_url, file_name)
    if check_size(file_name):
        post_image(bot, channel_id, file_name, comics_title)
        remove_comics(file_name)
    else:
        f'The size of the image {os.path.basename(file_name)} exceeds 20 MB.'


if __name__ == '__main__':
    main()