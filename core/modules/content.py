import tls_client
from datetime import datetime
from colorama import Fore
from core.modules.utils.general import extra  

def check(content, file):
    if content in file:
        return True
    return False

def content(self, url,  name, header, content):
    url = url.format(name)
    ed = "NO - ED"
    session = tls_client.Session()
    request = session.get(url, headers={'User-Agent': str(header)})
    if check(content, request.text):
        ed = extra(url, request.text)
        print(
            f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}][{Fore.LIGHTBLACK_EX}CONT{Fore.RESET}] [{url}] - [{ed}]"
        )
    self.total += 1