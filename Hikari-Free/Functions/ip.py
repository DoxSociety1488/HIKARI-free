# ip search by robert
from colorama import Fore, Style, init
import requests
import json
init()

dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()

    return data

def get_ip_type(ip_address):
    url = f"https://ipwho.is/{ip_address}"
    response = requests.get(url)
    ip_info = response.json()

    return ip_info

def ipsearch(ip_address):
    ip_info = get_ip_info(ip_address)
    print(f" {white}ОБЩАЯ ИНФОРМАЦИЯ: ")
    if 'ip' in ip_info:
        print(f"{dcyan}[{white}+{dcyan}]{cyan} IP-адрес:{white}", ip_info['ip'])
        ip_type_info = get_ip_type(ip_address)

    else:
        print(f"{dcyan}[{white}-{dcyan}]{cyan} IP-адрес недоступен")

    if 'city' in ip_info:
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Город:{white}", ip_info['city'])
    else:
        print(f"{dcyan}[{white}-{dcyan}]{cyan} Город недоступен")
    
    if 'region' in ip_info:
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Регион:{white}", ip_info['region'])
    else:
        print(f"{dcyan}[{white}-{dcyan}]{cyan} Регион недоступен")


    print(f"{dcyan}[{white}+{dcyan}]{cyan} Континент:{white}", ip_type_info['continent'], ip_type_info['continent_code'] )
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Страна:{white}", ip_type_info['country'], ip_type_info['country_code'] )
    
    



    print(f"{dcyan}[{white}+{dcyan}]{cyan} Почтовый Индекс:{white}", ip_type_info['postal'])
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Код Телефона:{white}",ip_type_info['calling_code'])
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Языки:{white}",ip_type_info['borders'])
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Часовой пояс:{white}", ip_info['timezone'])


    print(f"{white} ГЕОЛОКАЦИЯ: ")

    if 'loc' in ip_info:
        latitude, longitude = ip_info['loc'].split(',')
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Координаты:{white}", ip_info['loc'])
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        yandex_maps_url = f"https://yandex.ru/maps/?ll={longitude},{latitude}&z=10"
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Ссылка на Google Maps:{white}", google_maps_url)
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Ссылка на Yandex Maps:{white}", yandex_maps_url)

    else:
        print(f"{dcyan}[{white}-{dcyan}]{cyan} Координаты недоступны")

    print(f"{white} ТЕХНИЧЕСКАЯ ИНФОРМАЦИЯ: ")

    print(f"{dcyan}[{white}+{dcyan}]{cyan} Тип IP-адреса:{white}", ip_type_info['type'])
    if 'hostname' in ip_info:
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Hostname:{white}", ip_info['hostname'])
    else:
        print(f"{dcyan}[{white}-{dcyan}]{cyan} Hostname недоступен")
        
    if 'org' in ip_info:
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Организация:{white}", ip_info['org'])
    print(f"{white} ПОИСК IP В IoT: ")
    shodan_url = f"https://www.shodan.io/search?query={ip_address}"
    censys_url = f"https://censys.io/ipv4/{ip_address}"
    zoomeye_url = f"https://www.zoomeye.org/searchResult?q={ip_address}"
    criminalip_url = f"https://www.criminalip.io/asset/report/{ip_address}"
    virustotal_url = f"https://www.virustotal.com/gui/ip-address/{ip_address}"
    
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Shodan: {white}{shodan_url}")
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Censys: {white}{censys_url}")
    print(f"{dcyan}[{white}+{dcyan}]{cyan} Zoomeye: {white}{zoomeye_url}")
    print(f"{dcyan}[{white}+{dcyan}]{cyan} CriminalIP: {white}{criminalip_url}")
    print(f"{dcyan}[{white}+{dcyan}]{cyan} VirusTotal: {white}{virustotal_url}")
