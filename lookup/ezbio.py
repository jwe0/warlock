import requests

def search(data):
    for line in data.splitlines():
        if ",\"name\":\"" in line:
            return line.split(",\"name\":\"")[1].split("\"")[0]