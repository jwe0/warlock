import requests, json, sys, threading, random, atexit, time
from datetime import datetime
from pyfiglet import Figlet
from colorama import Fore
from pystyle import Center, Colorate, Colors

hits = 0
total = 0
start = 0
user = ""


class Main:
    def check(url, name, position, adj, header):
        global hits
        url = url.format(name)
        try:
            request = requests.get(url, headers={'User-Agent' : str(header)})

            if request.status_code == 200:
                hits += 1
                print(f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.GREEN}{str(position).rjust(adj, '0')}{Fore.RESET}] [{url}]")
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

        print(f"\n[{Fore.YELLOW}+{Fore.RESET}] Scanned {total} for \"{user}\" and got {hits} results in {int(time.time() - start)}s")


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
                threading.Thread(target=Main.check, args=[url[1], username, completed, len(str(file_lines)), random.choice(agents)]).start()



if __name__ == "__main__":
    atexit.register(Main.exit_func)
    Main.Main()
