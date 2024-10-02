import json, sys, threading, random
from core.modules.utils.general import art
from core.modules.content import content
from core.modules.title   import title
from core.modules.status  import status

hits = 0
total = 0
start = 0
user = ""

class Main:
  def __init__(self) -> None:
    self.hits  = 0
    self.total = 0
    self.start = 0
    self.user  = ""


  def get_lines(self, file):
    return len(json.load(open(file)))

  def agents(self):
    return (open("Firefox.txt").readlines())

  def main(self):
    art()
    self.user = sys.argv[1]
    site_list = "Sites/sites.json" if len (sys.argv) == 2 else sys.argv[2]
    agents = open("core/assets/Firefox.txt").readlines()

    file = json.load(open(site_list))
    for site in file:
      site_ = file[site]
      if site_["type"] == "site-content":
        content(self, site_["url"], self.user, random.choice(agents).strip(), site_["check-value"])
      elif site_["type"] == "title-content":
        title(self, site_["url"], self.user, random.choice(agents).strip(), site_["check-value"])
      elif site_["type"] == "status-code":
        status(self, site_["url"], self.user, random.choice(agents).strip(), site_["check-value"])
      
    while self.total < self.get_lines(site_list):
      pass
    
if __name__ == "__main__":
  main = Main()
  main.main()