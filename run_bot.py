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

    comics_title, comics_image_url = get_random_comics_info()
    try:
        dowload_comics(comics_image_url, comics_title)
        
        if check_size(comics_title):
            post_image(bot, channel_id, comics_title)
            remove_comics(comics_title)
        else:
            print(f'The size of the image {os.path.basename(comics_title)} exceeds 20 MB.')
    finally:
        if os.path.exists(comics_title):
            remove_comics(comics_title)


if __name__ == '__main__':
    main()