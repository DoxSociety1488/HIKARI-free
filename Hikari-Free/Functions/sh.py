# thanks to robert 
import shodan
from colorama import Style, Fore, init

init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def shodanlookup():
    api_key = input(f"{dcyan}[{white}?{dcyan}]{cyan} Введите api-ключ от Shodan для поиска информации: ")
    target_ip = input(f"{dcyan}[{white}?{dcyan}]{cyan} Введите IP для поиска информации: ")
    api = shodan.Shodan(api_key)

    try:
        host = api.host(target_ip)
        print(f"{dcyan}[{white}!{dcyan}]{cyan} ОСНОВНАЯ ИНФОРМАЦИЯ [ ~ Shodan ] ")
        print("                    ")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} IP-адрес: {host['ip_str']}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Провайдер: {host.get('org')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Страна: {host.get('country_name')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Страны: {host.get('country')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Город: {host.get('city')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} ОС: {host.get('os')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Открытые порты:")
        for item in host['data']:
            print(f"Порт: {item['port']}, Протокол: {item['transport']}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Домены:")
        print(f"{host.get('domain')}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Автономные системы:")
        print(f"{host.get('asn')}")


    except shodan.APIError as e:
        print(f"{dcyan}[{white}!{dcyan}]{cyan} Произошла ошибка: {e}")


