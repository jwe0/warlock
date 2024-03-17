import requests

def search(data):
    for line in data.splitlines():
        if "profile-name" and "h1" in line:
            return line.split(">")[1].replace("</h1", "")
            