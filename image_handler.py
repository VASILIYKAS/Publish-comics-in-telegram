import os


def check_size(file_name):
    twenty_megabytes = 20000000

    size_image = os.path.getsize(file_name)
    return size_image < twenty_megabytes
    

def remove_comics(file_name):
    os.remove(file_name)