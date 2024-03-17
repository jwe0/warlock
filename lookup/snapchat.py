import requests

def search(data):
    for line in data.splitlines():
        if "<title" in line:
            return line.split("<title")[1].split("|")[0].split(">")[1]