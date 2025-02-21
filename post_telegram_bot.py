

def post_image(bot, channel_id, comics_title):
    if not comics_title:
        return 'No images found in the directory.'

    if comics_title:
        send_commics(bot, channel_id, comics_title)
    else:
        return 'The image name is incorrect. Such an image was not found.'
    

def send_commics(bot, channel_id, comics_title):
    with open(comics_title, 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo, caption=comics_title)
