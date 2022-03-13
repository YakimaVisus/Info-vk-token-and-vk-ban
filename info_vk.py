# -*- coding: utf-8 -*-
import vk_api
import requests
from vk_api.longpoll import VkLongPoll
print(f'By Yakima Visus \n узнаем инфу по токену \n Гитхаб: https://github.com/YakimaVisus \n')
token = input("Токен вк: ")

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session,id)

fa = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["first_name"] 
ids = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&v=5.103").json()["response"][0]["id"]                                        
ln = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["last_name"] 
ht = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["home_town"]
na = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["phone"]
datas = requests.get(f"https://api.vk.com/method/account.getProfileInfo?access_token={token}&v=5.103").json()["response"]["bdate"]
fc = requests.get(f"https://api.vk.com/method/users.get?access_token={token}&fields=followers_count&v=5.103").json()["response"][0]["followers_count"]
gp = requests.get(f"https://api.vk.com/method/groups.get?access_token={token}&v=5.103").json()["response"]["count"]
ag = requests.get(f"https://api.vk.com/method/groups.get?access_token={token}&filter=admin&v=5.103").json()["response"]["count"]
fr = requests.get(f"https://api.vk.com/method/friends.get?access_token={token}&v=5.103").json()["response"]["count"]
print(f''' Информация по Аккаунту: 
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
---------------------------------
''')