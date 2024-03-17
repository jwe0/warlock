import requests


def search(data):
  for line in data.splitlines():
    if "<title>" in line:
      return line.replace(" <title>", "").replace(" · GitHub</title>", "")