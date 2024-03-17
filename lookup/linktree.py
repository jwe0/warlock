import requests

def search(data):
    for line in data.splitlines():
        if "<h1 id=\"profile-" in line:

            return  line.split("<h1 id=\"profile-")[1].split("\"")[0]