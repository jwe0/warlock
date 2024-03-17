import requests

def search(data):
    print(data)
    for line in data.splitlines():
        if "<title>" in line:
            print(line)