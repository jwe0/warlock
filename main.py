import requests, json, sys, threading, random, atexit, time, json, sys
from datetime import datetime
from pyfiglet import Figlet
from colorama import Fore
from requests_html import HTMLSession, AsyncHTMLSession
from lookup import github, replit, devto, soloto, pornhub, snapchat, onlymyspace, linktree, allmylinks, ezbio
from pystyle import Center, Colorate, Colors

hits = 0
total = 0
start = 0
user = ""



class Main:

  def check_status(url, name, position, adj, header, code):
    global hits
    url = url.format(name)
    ed = "NO - ED"
    try:
      session = HTMLSession()
      request = session.get(url, headers={'User-Agent': str(header)})

      if request.status_code == code:
        if "github" in url:
          ed = github.search(request.text)
        elif "replit" in url:
          ed = replit.search(request.text)
        elif "dev.to" in url:
          ed = devto.search(request.text)
          ed = ed.get("name")
        elif "pornhub" in url:
          ed = pornhub.search(request.text)
        elif "snapchat" in url:
          ed = snapchat.search(request.text)
        elif "only-my.space" in url:
          ed = onlymyspace.search(request.text) 
        elif "linktr.ee" in url:
          ed = linktree.search(request.text)
        elif "allmylinks" in url:
          ed = allmylinks.search(request.text)
        elif "e-z.bio" in url:
          ed = ezbio.search(request.text)


        hits += 1
        print(
            f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.GREEN}{str(position).rjust(adj, '0')}{Fore.RESET}] [{Fore.LIGHTBLACK_EX}STAT{Fore.RESET}] [{url}] - [{ed}]"
        )

    except:
      pass



  def check_content(url, name, position, adj, header, content):
    global hits
    url = url.format(name)
    ed = "NO - ED"
    try:
      session = HTMLSession()
      request = session.get(url, headers={'User-Agent': str(header)})

      if content not in request.text:

      


        if "github" in url:
          ed = github.search(request.text)
        elif "replit" in url:
          ed = replit.search(request.text)
        elif "dev.to" in url:
          ed = devto.search(request.text)
          ed = ed.get("name")
        elif "pornhub" in url:
          ed = pornhub.search(request.text)
        elif "snapchat" in url:
          ed = snapchat.search(request.text)
        elif "only-my.space" in url:
          ed = onlymyspace.search(request.text) 
        elif "linktr.ee" in url:
          ed = linktree.search(request.text)
        elif "allmylinks" in url:
          ed = allmylinks.search(request.text)
        elif "e-z.bio" in url:
          ed = ezbio.search(request.text)


        hits += 1
        print(
            f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.GREEN}{str(position).rjust(adj, '0')}{Fore.RESET}] [{Fore.LIGHTBLACK_EX}CONT{Fore.RESET}] [{url}] - [{ed}]"
          )

    except:
      pass

  def check_title(url, name, position, adj, header, content):
    global hits
    url = url.format(name)
    ed = "NO - ED"
    try:
      session = HTMLSession()
      request = session.get(url, headers={'User-Agent': str(header)})

      for line in request.text.splitlines():
        
        if "<title>" in line:
          if content not in line:

            if "github" in url:
              ed = github.search(request.text)
            elif "replit" in url:
              ed = replit.search(request.text)
            elif "dev.to" in url:
              ed = devto.search(request.text)
              ed = ed.get("name")
            elif "pornhub" in url:
              ed = pornhub.search(request.text)
            elif "snapchat" in url:
              ed = snapchat.search(request.text)
            elif "only-my.space" in url:
              ed = onlymyspace.search(request.text) 
            elif "linktr.ee" in url:
              ed = linktree.search(request.text)
            elif "allmylinks" in url:
              ed = allmylinks.search(request.text)
            elif "e-z.bio" in url:
              ed = ezbio.search(request.text)


            hits += 1
            print(
                f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.GREEN}{str(position).rjust(adj, '0')}{Fore.RESET}] [{Fore.LIGHTBLACK_EX}TITS{Fore.RESET}] [{url}] - [{ed}]"
              )

    except:
      pass







  def get_lines(file):
    return len(open(file).readlines())

  def agents():
    return (open("Firefox.txt").readlines())

  def tits(name):
    f = Figlet(font='calvin_s')
    return f.renderText(name)

  def exit_func():
    global hits
    global total
    global user
    global start

    print(
        f"\n[{Fore.YELLOW}+{Fore.RESET}] Scanned {total} for \"{user}\" and got {hits} results in {int(time.time() - start)}s"
    )

  def Main():
    global total
    global start
    global user

    art = """
                  .

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\  I     .            ╦ ╦╔═╗╦═╗╦  ╔═╗╔═╗╦╔═
  \].`[/  I                 ║║║╠═╣╠╦╝║  ║ ║║  ╠╩╗
  /l\/j\  (]    .  O        ╚╩╝╩ ╩╩╚═╩═╝╚═╝╚═╝╩ ╩
 /. ~~ ,\/I          .     
 \ L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o    Made by Josh Webb
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\_
        
        """
    print(Colorate.Vertical(Colors.blue_to_cyan, Center.XCenter(art)))
    username = sys.argv[1]
    site_list = sys.argv[2]
    completed = 0
    user = username
    file_lines = Main.get_lines(site_list)
    agent_file = open("Firefox.txt").read()
    agents = [agent for agent in agent_file.splitlines()]
    with open(site_list) as f:
      start = time.time()
      config = json.load(f)
      for url in config.items():
        total += 1
        completed += 1
        if url[1].get("type") == "status-code":
          threading.Thread(target=Main.check_status,args=[url[1].get("url"), username, completed,len(str(file_lines)),random.choice(agents), url[1].get("check-value")]).start()
        elif url[1].get("type") == "site-content":
          threading.Thread(target=Main.check_content,args=[url[1].get("url"), username, completed,len(str(file_lines)),random.choice(agents), url[1].get("check-value")]).start()
        elif url[1].get("type") == "title-content":
          threading.Thread(target=Main.check_title,args=[url[1].get("url"), username, completed,len(str(file_lines)),random.choice(agents), url[1].get("check-value")]).start()

if __name__ == "__main__":
  atexit.register(Main.exit_func)
  Main.Main()
  #r = requests.get("https://www.snapchat.com/add/database", headers={'User-Agent' : "Mozilla/5.0 (Windows NT 5.0; Windows NT 5.1; Windows NT 6.0; Windows NT 6.1; Linux; es-VE; rv:52.9.0) Gecko/20100101 Firefox/52.9.0"}).text
  #snapchat.search(r)