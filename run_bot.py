import os
from dotenv import load_dotenv
from telegram import Bot
from fetch_comics import get_random_comics_info
from image_handler import get_file_name
from image_downloader import dowload_comics
from post_telegram_bot import post_image


def main():
    load_dotenv()

    tg_token = os.environ['TG_TOKEN']
    bot = Bot(token=tg_token)
    channel_id = os.environ['TG_CHAT_ID']

    comics_title, comics_image_url = get_random_comics_info()
    file_name = get_file_name(comics_image_url, comics_title)

    dowload_comics(comics_image_url, file_name)

    post_image(bot, channel_id, file_name, comics_title)


if __name__ == '__main__':
    main()