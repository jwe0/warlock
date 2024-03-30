# Warlock

```
                  .

                   .
         /^\     .
    /\   "V"
   /__\   I      O  o
  //..\  I     .            ╦ ╦╔═╗╦═╗╦  ╔═╗╔═╗╦╔═
  \].`[/  I                 ║║║╠═╣╠╦╝║  ║ ║║  ╠╩╗
  /l\/j\  (]    .  O        ╚╩╝╩ ╩╩╚═╩═╝╚═╝╚═╝╩ ╩
 /. ~~ ,\/I          .
 \\L__j^\/I       o
  \/--v}  I     o   .
  |    |  I   _________
  |    |  I c(`       ')o
  |    l  I   \.     ,/
_/j  L l\_!  _//^---^\\_
```


Warlock is a simple python based social media discovery tool, it leverages how social media platforms will handle existing and non existing social media status codes. (existing = 200 non exsiting = 404). Warlock uses threading to scan multiple websites at the same time. This tool is inspired by sherlock `https://github.com/sherlock-project/sherlock`.

# Features
Warlock will also attempt to pull extra data from certain websites this can be useful when identifying if a site is actually your targets. My other osint tool "Mage" uses the same sort of code to pull even more information.

# Usage
1. Install  the repository with `git clone https://github.com/jwe0/warlock`
2. Change directory into the folder with `cd warlock`
3. Run `pip install -r requirements.txt` to install the requirements needed
4. When installed run `python main.py [target-username] [site-list]`
5. Reap your rewards

# To do list
* [x] Push latest update
* [x] Push new database


# Regards
Credits to the sherlock team for the status code websites.

# Regards
I take no legal responsibility for any negative actions committed with my software. This was made for ethical purposes only <3.
