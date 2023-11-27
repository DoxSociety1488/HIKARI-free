import re
import os
from time import sleep
from colorama import Fore, Style, init
init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def custom_database():
    try:
        print(f"\n{dcyan}[{white}~{dcyan}]{cyan} Пример : C:\\Users\\Admin\\Desktop\\Soft\\GetContact.csv \n{dcyan}[{white}~{dcyan}]{cyan} Или же поместите базу в одну папку с софтом и укажите название файла с расширением"
                  f"\n{dcyan}[{white}~{dcyan}]{cyan} Также не забывайте указывать расширение базы данных!")

        file_path = input(f"\n{dcyan}[{white}?{dcyan}]{cyan} Введите путь к базе данных : ")
        search_text = input(f"{dcyan}[{white}?{dcyan}]{cyan} Введите параметр, по которому хотите найти информацию в бд : ")
        coder = input(f"{dcyan}[{white}?{dcyan}]{cyan} Выберите кодировку (Часто это utf-8 либо cp1251) : ")

        def scan_file(file_path, search_text):
            if os.path.exists(file_path):
                print(f"\n{dcyan}[{white}~{dcyan}]{cyan} Файл найден!")
                sleep(1)
                print(f"\n{dcyan}[{white}~{dcyan}]{cyan} Провожу сканирование...")
                sleep(1)
                try:
                    lines_with_text = []
                    with open(file_path, 'r', encoding=f'{coder}', errors='ignore') as file:
                        for line in file:
                            if search_text in line:
                                if re.search(search_text, line, flags=re.IGNORECASE):
                                    lines_with_text.append(line.strip())
                    return lines_with_text
                except Exception as e:
                    return f"\n{dcyan}[{white}!{dcyan}]{cyan} Ошибка! : {e}"
            else:
                print(f"\n{dcyan}[{white}!{dcyan}]{cyan} Файл не обнаружен!")

        result1 = scan_file(file_path, search_text)
        if result1 == []:
            print(f"\n{dcyan}[{white}!{dcyan}]{cyan} Ничего не найдено!")
        else:
            print(f"\n{dcyan}[{white}~{dcyan}]{cyan} Информация найденная в соотвествии с вашим запросом:"
                  f"\n{dcyan}[{white}+{dcyan}]{cyan}", result1)
    except:
        print(f'\n{dcyan}[{white}+{dcyan}]{cyan} Произошла ошибка! Проверьте ввод данных!')