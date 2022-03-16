# -*- coding: utf-8 -*-
import requests
print(f'By Yakima Visus \n узнаем инфу по токену \n Гитхаб: https://github.com/YakimaVisus \n')
token = input("Токен вк: ")
def call(method, options={}, **kwargs):
    '''Фукнция вызова api ВК.'''
    options['access_token'] = token
    options['v'] = '5.103'
    options.update(kwargs)
    resp = requests.get('https://api.vk.com/method/'+method, params=options).json()
    if 'error' in resp:
        print('VKERROR: {error_code}: {error_msg}'.format(**resp['error']))
    return resp
fa = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["first_name"]
ids = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v=5.103").json()["response"][0]["id"]
ln = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["last_name"]
my_file = open(f"{ids}.txt", "a+")

try:
    ht = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["home_town"]
except:
    ht = "None"
try:
    na = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["phone"]
except:
    na = "None"
try:
    datas = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["bdate"]
except:
    datas = "None"
try:
    fc = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&fields=followers_count&v=5.103").json()["response"][0]["followers_count"]
except:
    fc = "None"
try:
    co = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["country"]["title"]
except:
    co = "None"
try:
    gp = requests.get(f"https://api.vk.com/method/groups.get?access_token={token}&v=5.103").json()["response"]["count"]
except:
    gp = "None"
try:
    ag = requests.get(f"https://api.vk.com/method/groups.get?access_token={token}&filter=admin&v=5.103").json()["response"]["count"]
except:
    ag = "None"
try:
    fr = requests.get(f"https://api.vk.com/method/friends.get?access_token={token}&v=5.103").json()["response"]["count"]
except:
    fr = "None"
try:
    fr1 = requests.get(f"https://api.vk.com/method/friends.get?access_token={token}&v=5.103").json()["response"]["hints"]
except:
    fr1 = "None"
log = (f''' Информация по Аккаунту:
---------------------------------
|Фамилия Имя: {fa} {ln}
|
|Ссылка:  https://vk.com/id{ids}
|
|Телефон: {na}
|
|Дата рождения: {datas}
|
|Количество друзей: {fr}
|
|Количество подписчиков: {fc}
|
|Количество групп: {gp}
|
|Админ в группе: {ag}
|
|Возможный адрес: {co}

    создана папка с данными
---------------------------------
''')
print(log)
my_file.write(log)
