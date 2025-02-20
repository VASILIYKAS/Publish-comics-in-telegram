import os

def post_image(bot, channel_id, file_name, comics_title):
    if not file_name:
        return 'No images found in the directory.'

    if file_name:
        send_image(bot, channel_id, file_name, comics_title)
    else:
        return 'The image name is incorrect. Such an image was not found.'
    

def send_image(bot, channel_id, file_name, comics_title):
    twenty_megabytes = 20000000

    size_image = os.path.getsize(file_name)
    if size_image < twenty_megabytes:
        with open(file_name, 'rb') as photo:
            bot.send_photo(chat_id=channel_id, photo=photo, caption=comics_title)
    else:
        return f'The size of the image {os.path.basename(file_name)} exceeds 20 MB.'
    
    os.remove(file_name)