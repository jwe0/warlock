import requests


def search(data):
  r = requests.get("https://replit.com/@Myepicschoolgit")
  with open("test", 'r') as f:
    for line in f.read().splitlines():
      if "<title>" in line:
        return line.split("<title>")[1].split("</title>")[0].replace(" - Replit", "")
