import os
from random import choices
import string

short_link_length = int(os.getenv("SHORT_LINK_LENGTH", 6))


def generate_short_link(length=short_link_length):
    characters = string.digits + string.ascii_letters
    short_url = "".join(choices(characters, k=length))

    return short_url
