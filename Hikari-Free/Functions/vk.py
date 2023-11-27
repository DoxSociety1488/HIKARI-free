import requests
from colorama import Fore, Style, init

dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL

def vkinfo(user_id, access_token):
    fields = 'sex,bdate,city,country,photo_200_orig,home_town,domain,status,followers_count,common_count,about,activities,can_post,can_see_all_posts,can_see_audio,can_send_friend_request,can_write_private_message,career,connections,contacts,counters,exports,is_no_index,relatives'
    url = f'https://api.vk.com/method/users.get?user_ids={user_id}&fields={fields}&access_token={access_token}&v=5.131'


    response = requests.get(url)
    data = response.json()
    user_data = data['response'][0]

    user_info = {
        'Имя': user_data['first_name'],
        'Фамилия': user_data['last_name'],
        'ID': user_data['id'],
        'Ссылка на профиль': f'https://vk.com/id{user_data["id"]}',
        'Пол': 'Мужской' if user_data['sex'] == 2 else 'Женский',
        'Дата рождения': user_data.get('bdate', 'Не указана'),
        'Город': user_data.get('city', {}).get('title', 'Не указан'),
        'Страна': user_data.get('country', {}).get('title', 'Не указан'),
        'Фото профиля': user_data.get('photo_200_orig', 'Фото отсутствует'),
        'Родной город': user_data.get('home_town', 'Не указан'),
        'Короткий адрес страницы': user_data.get('domain', 'Не указан'),
        'Статус': user_data.get('status', 'Статус не указан'),
        'Количество подписчиков': user_data.get('followers_count', 'Информация недоступна'),
        'Количество общих друзей': user_data.get('common_count', 'Информация недоступна'),
        'О себе': user_data.get('about', 'Информация недоступна'),
        'Деятельность': user_data.get('activities', 'Информация недоступна'),
        'Может оставлять записи на стене': 'Да' if user_data.get('can_post') == 1 else 'Нет',
        'Может видеть чужие записи на стене': 'Да' if user_data.get('can_see_all_posts') == 1 else 'Нет',
        'Может видеть аудиозаписи': 'Да' if user_data.get('can_see_audio') == 1 else 'Нет',
        'Уведомление о заявке в друзья': 'Отправлено' if user_data.get('can_send_friend_request') == 1 else 'Не отправлено',
        'Может отправить личное сообщение': 'Да' if user_data.get('can_write_private_message') == 1 else 'Нет',
        'Карьера': user_data.get('career', []),
        'Социальные связи': user_data.get('connections', {}),
        'Контактная информация': user_data.get('contacts', {}),
        'Счётчики': user_data.get('counters', {}),
        'Экспорт во внешние сервисы': user_data.get('exports', {}),
        'Индексируется поисковыми сайтами': 'Да' if user_data.get('is_no_index') == 0 else 'Нет',
        'Родственники': user_data.get('relatives', []),
        }
    user_info['Имя'] = user_info['Имя'].capitalize()
    user_info['Фамилия'] = user_info['Фамилия'].capitalize()
    print(' ')
    for key, value in user_info.items():
        print(f'{dcyan}[{white}+{dcyan}]{cyan} {key} : {value}')

