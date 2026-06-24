---
title: "Підключення сервера до домашньої мережі через VPN"
category: "networking"
tags: ['create', 'докера', 'gateway', 'sudo', 'network']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿
1   -----------
2   Связи: [[docker докер]] [[Встановлення Docker установка докера]] 
3   Теги:
## - підключаюсь до серверу
sudo server    
## - заходжу в [[контейнер]] з докерфайлом
cd sharko/container/
## - Створюю **мережу** з параметрами, що дозволяють доступ до моєї локальної мережі:
docker network create --subnet=172.18.0.0/16 --gateway=172.18.0.1 my_custom_network
  Запустіть контейнер в цій мережі:
## - Запускаю контейнер в цій мережі:
docker run --rm -it --privileged --network my_custom_network --ip 172.18.0.2 my-kali-container



kkkkk
## Налаштування VPN (ZeroTier)
-  Встановлення ZeroTier на сервер
curl -s https://install.zerotier.com | sudo bash

Підключення сервера до ZeroTier мережі
Встановлення ZeroTier на домашній ПК
Завантажую з офіційного сайту.
 це для підключення :  565799d8f6eeb94b
 sudo zerotier-cli join 565799d8f6eeb94b    - обовязково судо примінити

перевірити зєднання :
sudo zerotier-cli status
вивід правильного зєднання :
200 info 9da1dd2c99 1.14.2 ONLINE




це згенеровано на сайті ZeroTier
NETWORK ID   565799d8f6eeb94b
NAME               hopeful_heatherington
DESCRIPTION
SUBNET          192.168.193.0/24	
NODES             0
CREATED          2025-01-13

 **авторизація** тут : https://accounts.zerotier.com