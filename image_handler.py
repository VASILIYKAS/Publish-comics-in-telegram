import os


def check_size(comics_title):
    twenty_megabytes = 20000000

    size_image = os.path.getsize(comics_title)
    return size_image < twenty_megabytes
    

def remove_comics(comics_title):
    os.remove(comics_title)