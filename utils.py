import os
from slugify import slugify


def next_path(path_pattern):
    i = 1
    while os.path.exists(path_pattern % i):
        i += 1
    return path_pattern % i


def get_file_name(name):
    name, ext = os.path.splitext(name)
    name = slugify(name)
    return next_path(os.path.join('uploads', name) + '%d' + ext)
