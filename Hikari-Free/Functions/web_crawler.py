from bs4 import BeautifulSoup
from urllib.parse import urljoin
from colorama import Style, Fore, init
import requests

init()

dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def web_crawler(url, depth):
    try:
        visited = set()
        queue = [(url, 0)]

        while queue:
            current_url, current_depth = queue.pop(0)

            if current_url in visited or current_depth > depth:
                continue

            visited.add(current_url)
            print("{dcyan}[{white}!{dcyan}]{cyan} Ссылка:", current_url)

            try:
                response = requests.get(current_url)
                soup = BeautifulSoup(response.text, 'html.parser')

                for link in soup.find_all('a', href=True):
                    absolute_url = urljoin(current_url, link['href'])
                    queue.append((absolute_url, current_depth + 1))
            except Exception as e:
                print("Ошибка:", e)
    except:
        print(f'\n{dcyan}[{white}!{dcyan}]{cyan} Произошла ошибка! Проверьте ввод данных!')
