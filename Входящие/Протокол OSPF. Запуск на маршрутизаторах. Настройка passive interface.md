---
title: "Протокол OSPF. Запуск на маршрутизаторах. Настройка passive interface"
category: "networking"
tags: ['організація', 'маршрутизація', 'статичного', 'налаштування', 'ospf']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------Cisko

2   Связи:  [[Налаштування  протоколу SSH для доступу на комутатор]] , [[налаштування статичного маршруту]] , [[Multi-hop(ова) статична маршрутизація]] , [[Налаштування пріоритетів у статичних маршрутів, організація резервного маршруту]] , [[Налаштування пріоритетів у статичних маршрутів організація резервного маршруту продовження]] [[Організація маршруту за замовчуванням]] , [[Протокол OSPF. Запуск на маршрутизаторах. Настройка passive interface]] , 
3   Теги [[Протокол OSPF. Запуск на маршрутизаторах. Настройка passive interface]]
kino:https://www.youtube.com/watch?v=IdPz3oT2ZTk

Перед початком роботи було розміщено пристрої, проведені і помарковані мережі, задано ІР адреси кінцевим пристроям а також проведено деякі налаштування маршрутизаторів.:
задано імя, та була активована команда
loggining synchronous
hostname R?
no ip domain-lookup
line console 0
logging synchronous
do wr
Виконую **налаштування інтерфейсів** маршрутизаторів
у **R1**
interface fastEthernet 0/0
no sh
ip address 192.168.100.1 255.255.255.248
int fa 0/1
no sh
ip address 192.168.100.73 255.255.255.252
int eth 0/1/0
no sh
ip address 192.168.100.85 255.255.255.252
у **R2**
interface fastEthernet 0/0
no sh
ip address 192.168.100.77 255.255.255.252
int fa 0/1
no sh
ip address 192.168.100.74 255.255.255.252
do wr
у **R3**
interface fastEthernet 0/0
no sh
ip address 192.168.100.9 255.255.255.248
int fa 0/1
no sh
ip address 192.168.100.78 255.255.255.252
do wr
int eth 0/0/0
no sh
ip address 192.168.100.81 255.255.255.252
do wr
у **R4**
int eth 0/0/0
no sh
ip address 192.168.100.82 255.255.255.252
int eth 0/1/0
no sh
ip address 192.168.100.86 255.255.255.252
do wr
запуск протоколу OSPF
**R1**
router ospf 1 (надаю процесу протоколу номер процесу 1)
do sh ip ro
network 192.168.100.0 0.0.0.7 area 0   (де 0.0.0.7 **зворотня маска**  area 0 **номер зони**)
network 192.168.100.72 0.0.0.3 area 0
network 192.168.100.84 0.0.0.3 area 0
router-id 1.1.1.1 ( вказую **ідентифікатор роутера** в мережі у вигляді ІР адреси 1.1.1.1)
do wr
**R2**
router ospf 2 (надаю процесу протоколу номер процесу 2)
router-id 2.2.2.2 ( вказую **ідентифікатор роутера** в мережі у вигляді ІР адреси 2.2.2.2)
do sh ip ro
network 192.168.100.0 0.0.0.7 area 0   (де 0.0.0.7 **зворотня маска**  area 0 **номер зони**)
network 192.168.100.72 0.0.0.3 area 0
network 192.168.100.76 0.0.0.3 area 0
do wr
**R3**
router ospf 3
router-id 3.3.3.3
do sh ip ro
network 192.168.100.8 0.0.0.7 area 0
network 192.168.100.76 0.0.0.3 area 0
network 192.168.100.80 0.0.0.3 area 0
do wr
**R4**
router ospf 4
router-id 4.4.4.4
do sh ip ro
network 192.168.100.80 0.0.0.3 area 0
network 192.168.100.84 0.0.0.3 area 0
do wr
щоб подивитися **метрику** інтерфейсу потрібно на маршрутизаторі в режимі **en** привілейованого режиму ввести команду:
show ip interface fastEthernet 0/1
щоб пакети не попадали до кінцевих користувачів потрібно зробити **налаштування пасивних інтерфейсів** 
**R1**
router ospf 1
passive-interface fastEthernet 0/0
do wr
**R3**
router ospf 
passive-interface fastEthernet 0/0
do wr