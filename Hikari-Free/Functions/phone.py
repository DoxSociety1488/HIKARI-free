from colorama import Fore, Style, init
from phonenumbers import geocoder, carrier, timezone
import phonenumbers
init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL
# Вывод информации
def phoneinfo(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return f"{dcyan}[{white}!{dcyan}]{cyan} Недействительный номер телефона"
        
        region_info = phonenumbers.geocoder.description_for_number(parsed_number, "ru")
        carrier_info = phonenumbers.carrier.name_for_number(parsed_number, "en")

        country = phonenumbers.geocoder.description_for_number(parsed_number, "en")
        region = phonenumbers.geocoder.description_for_number(parsed_number, "ru")
        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        timezona = timezone.time_zones_for_number(parsed_number)
        
        print(f"{white}Найденная информация:{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Номер телефона: {white}{formatted_number}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Страна: {white}{country}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Регион: {white}{region}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Оператор: {white}{carrier_info}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Активен?: {white}{is_possible}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Валид?: {white}{is_valid}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Таймзона: {white}{timezona}{blueb}")
        print(f"{white}Социальные сети:{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Telegram: {white}https://t.me/{phone_number}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Whatsapp: {white}https://wa.me/{phone_number}{blueb}")
        print(f"{dcyan}[{white}+{dcyan}]{cyan} Viber: {white}https://viber.click/{phone_number}{blueb}")
        
    except Exception as e:
        print(f"{dcyan}[{white}!{dcyan}]{cyan} Произошла ошибка: {str(e)}")
