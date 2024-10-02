import tls_client
from datetime import datetime
from colorama import Fore
from core.modules.utils.general import extra

def status(self, url, name, header, code):
    url = url.format(name)
    ed = "NO - ED"
    session = tls_client.Session()
    request = session.get(url, headers={'User-Agent': str(header)})

    if request.status_code == code:
        ed = extra(url, request.text)
        print(
            f"[{Fore.YELLOW}+{Fore.RESET}] [{Fore.LIGHTBLACK_EX}{datetime.now().strftime('%H:%M:%S')}{Fore.RESET}] [{Fore.GREEN}{request.status_code}{Fore.RESET}] [{Fore.LIGHTBLACK_EX}STAT{Fore.RESET}] [{url}] - [{ed}]"
        )
    self.total += 1