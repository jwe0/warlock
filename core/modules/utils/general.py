from pystyle import Center, Colorate, Colors

from bs4 import BeautifulSoup as bs
from core.modules.lookup import allmylinks, devto, github, linktree, onlymyspace, pornhub, snapchat, soloto

def art():
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

def extra(url, text):
  modules = {
     "github": github.search(text, bs),
     "dev.to": devto.search(text, bs),
     "pornhub": pornhub.search(text, bs),
     "snapchat": snapchat.search(text, bs),
     "only-my.space": onlymyspace.search(text, bs),
     "linktr.ee": linktree.search(text, bs),
     "allmylinks": allmylinks.search(text, bs),
     "soloto": soloto.search(text, bs)
  }
  for key, value in modules.items():
    if key in url:
      try:
        return value(text)
      except:
        return ""