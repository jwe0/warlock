import requests

def search(data):
    for line in data.splitlines():
        if "<title>" in line:
            return line.split("<title>")[1].replace("&#039;s Profile - Pornhub.com</title>", "")