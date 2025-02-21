

def post_image(bot, channel_id, file_name, comics_title):
    if not file_name:
        return 'No images found in the directory.'

    if file_name:
        send_commics(bot, channel_id, file_name, comics_title)
    else:
        return 'The image name is incorrect. Such an image was not found.'
    

def send_commics(bot, channel_id, file_name, comics_title):
    with open(file_name, 'rb') as photo:
        bot.send_photo(chat_id=channel_id, photo=photo, caption=comics_title)
