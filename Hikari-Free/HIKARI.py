# Заходи в наш тгк за обновлениями! t.me/projecthikari
from Other.opening import Banner, Menu
from Functions.phone import phoneinfo
from Functions.ip import ipsearch
from Functions.vk import vkinfo
from Functions.add_bd import custom_database
from Functions.wormgpt import wormgpt
from Functions.dos1 import dos1
from Functions.web_crawler import web_crawler
from Functions.sh import shodanlookup
from colorama import Fore, Style, init
init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL
# Соединение кода
def Main():
    Banner()
    Menu()
    Choose = input(f'{dcyan}[{white}?{dcyan}]{cyan} Ввод: ')
    if Choose == '1':
        number = input(f'{dcyan}[{white}?{dcyan}]{cyan} Номер телефона (Пример : +7XXXXXXXXXX): ')
        phoneinfo(number)
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '2':
        ip = input(f'{dcyan}[{white}?{dcyan}]{cyan} IP-адрес: ')
        ipsearch(ip)
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '3':
        apivk = input(f'{dcyan}[{white}?{dcyan}]{cyan} Vk-token : ')
        user_id = input(f'{dcyan}[{white}?{dcyan}]{cyan} Введите ID пользователя или короткую ссылку на страницу VK: ')
        if user_id.startswith('https://vk.com/'):
            user_id = user_id[len('https://vk.com/'):]
        vkinfo(user_id, apivk)
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '4':
        shodanlookup()
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '5':
        custom_database()
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '6':
        wormgpt()
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    if Choose == '7':
        dos1()
        Main()
    if Choose == '8':
        url = input(f'\n{dcyan}[{white}?{dcyan}]{cyan} Введите ссылку для кравлинга: ')
        web_crawler(url, depth=2)
        input(f'{dcyan}[{white}?{dcyan}]{cyan} Нажмите enter для продолжения ')
        Main()
    else:
        Main()
        
if __name__ == "__main__":
    Main()
