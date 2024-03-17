import requests

def search(data):
  found = False
  name = ""
  email = ""
  trigs = False

  results = {}
  

  for line in data.splitlines():
    if "<title>" in line and trigs != True:
      trigs = True
      name = line.split("    <title>")[1].replace(" - DEV Community</title>", "")
      results["name"] = name
      


  for line in data.splitlines():
    if "mailto:" in line:
      found = True
      email = line.split("mailto:")[1].split("class=")[0].replace('"', "")
      results["email"] = email

  return results


      