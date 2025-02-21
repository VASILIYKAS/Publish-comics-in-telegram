import os


def post_image(bot, channel_id, comics_title):
    if not comics_title or not os.path.exists(comics_title):
        raise FileNotFoundError(f'Комикс с именем {comics_title} не найден.')

    send_commics(bot, channel_id, comics_title)


def send_commics(bot, channel_id, comics_title):
    with open(comics_title, 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo, caption=comics_title)
