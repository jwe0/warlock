import requests

def search(data):
    for line in data.splitlines():
        if "uname" in line:
            return  line.split("uname")[1].split(",")[0].replace("\\", "").replace("\"", "").replace(":", "")