---
title: "Протокол OSPF Аутентификация пакетов с использованием алгоритма md5"
category: "networking"
tags: ['організація', 'маршрутизація', 'подключеные', 'статичного', 'налаштування']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿
2   Связи:  [[Налаштування  протоколу SSH для доступу на комутатор]] , [[налаштування статичного маршруту]] , [[Multi-hop(ова) статична маршрутизація]] , [[Налаштування пріоритетів у статичних маршрутів, організація резервного маршруту]] , [[Налаштування пріоритетів у статичних маршрутів організація резервного маршруту продовження]] [[Організація маршруту за замовчуванням]] , [[Протокол OSPF. Запуск на маршрутизаторах. Настройка passive interface]] , [[Протокол OSPF настройка метрики каналов между маршрутизаторами]] , [[Протокол OSPF настройка метрики каналов между маршрутизаторами]] [[Протокол OSPF настройка метрики каналов между маршрутизаторами]] , [[Протокол OSPF. Маршрутизация между разными зонами (area)]] , [[Порівняння OSI vs TCP  IP]] ,  [[Протокол OSPF. Объединяем области, не подключеные физически к Area 0]]
3   Теги  ,[[Протокол OSPF Аутентификация пакетов с использованием алгоритма md5]]

kino https://www.youtube.com/watch?v=pq4R8xdLf8w
створюю топологію і проводжу налаштування

задати власне шмя інтерфейсу:
description InputInterR3
description OutputInterR3
потім налаштувати протокол OSPF на маршрутизаторах
при налаштуванні не забути вказати пасивний інтерфейс (не пускати розсилку до клієнтських пристроїв) на кінцевих маршрутизаторах
passive-interface fa 0/0
приступаю до шифрування службової інформації . ключ шифрування не буде передаватися каналами звязку
**R1**
int fa 0/1
ip ospf message-digest-key 1 md5 123Ab
do wr
exit
router ospf 1
area 0 authentication message-digest
do wr
**R2**
int fa 0/1
ip ospf message-digest-key 1 md5 123Ab
do wr
exit
router ospf 2
area 0 authentication message-digest
do wr
**R2**   налаштовую інтерфейс до R3
int fa 0/0
ip ospf message-digest-key 2 md5 321aB
do wr
exit
router ospf 2
area 0 authentication message-digest
do wr

**R3**
int fa 0/0
ip ospf message-digest-key 2 md5 321aB
do wr
exit
router ospf 3
area 0 authentication message-digest
do wr

для наблюдання процесу використовування ключів також можна використовувати команду
debug ip ospf events
зупинити процес:
no debug ip ospf events