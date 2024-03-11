import requests, json, sys, threading
from datetime import datetime
from pyfiglet import Figlet
from colorama import Fore
from pystyle import Center, Colorate, Colors




class Main:
    def check(url, name, position, adj):
        url = url.format(name)
        try:
            request = requests.get(url)

            if request.status_code == 200:
                print(f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.GREEN}{str(position).rjust(adj, '0')}{Fore.RESET}] [{url}]")
        except Exception as f:
            pass


    def get_lines(file):
        return len(open(file).readlines())




    def tits(name):
        f = Figlet(font='calvin_s')
        return f.renderText(name)


    def Main():
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
        file_lines = Main.get_lines(site_list)
        with open(site_list) as f:
            config = json.load(f)
            for url in config.items():
                completed += 1
                threading.Thread(target=Main.check, args=[url[1], username, completed, len(str(file_lines))]).start()



if __name__ == "__main__":
    Main.Main()