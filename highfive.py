import os, utils, urllib.request
from PIL import Image

def create(avatar_url):
    os.system("wget {} -O h5_user.png".format(avatar_url))
    h5_base = Image.open("h5_base.png")
    h5_user = Image.open("h5_user.png")
    h5_base.paste(h5_user, (167, 28))
    h5_base.save("high5.png")

def remove():
    os.system("rm h5_user.png")
    os.system("rm high5.png")
