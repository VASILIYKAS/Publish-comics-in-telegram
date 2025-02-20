import os


def get_file_name(comics_image_url, comics_title):

    extension = os.path.splitext(comics_image_url)[1]
    file_name = comics_title + extension

    return file_name