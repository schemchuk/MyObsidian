---
title: "IP адрес от DHCP сервера, находящегося в сети другог маршрутизатора"
category: "networking"
tags: ['mnylqjilclq', 'сервера', 'порівняння', 'моделі', 'youtube']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи:[[порівняння моделі OSI (7 рівнів) та TCP IP (4 рівні)]]
3   Теги:[[VLAN]]
kino https://www.youtube.com/watch?v=MnYlQJIlClQ
заповнюю поля статичних компів і сервера
роблю на SW0 [[VLAN]]
**SW0**
Спочатку стандартні
потім влани
vlan 100
ex
vlan 101
ex
vlan 102
ex

int fa 0/1
switchport mode access
switchport access vlan 101
ex
int fa 0/2
switchport mode access
switchport access vlan 102
ex
int fa 0/24
switchport mode trunk
switchport trunk native vlan 100
do wr
ex
ex
sh vlan brief
**R1**
int fa 0/0
no sh
ip address 192.168.201.1 255.255.255.0
do wr
int eth 0/1/0
no sh
ip address 192.168.50.2 255.255.255.0
do wr
**R0**
int fa 0/0
no sh
int fa 0/0.101
encapsulation dot1Q 101
ip address 192.168.101.1 255.255.255.0
int fa 0/0.102
encapsulation dot1Q 102
ip address 192.168.102.1 255.255.255.0

int eth 0/1/0
no sh
ip address 192.168.50.1 255.255.255.0
do wr

int fa 0/1
no sh
ip address 192.168.51.1 255.255.255.0
**R2**
int fa 0/1
no sh
ip address 192.168.51.2 255.255.255.0
int fa 0/
no sh
ip address 192.168.11.1 255.255.255.0

після чого запускаю протокол маршрутизації  RIP. при запуску протокола будуть використовуватися пасивні мережі, щоб дані протоколу не доходили до кінцевих споживачів(клієнтів)
**R1**
router rip
version 2
no auto-summary

do sh ip ro
network 192.168.50.0
network 192.168.201.0
passive-interface fa 0/0
do wr
**R0**
router rip
version 2
no auto-summary

do sh ip ro
network 192.168.50.0
network 192.168.51.0
network 192.168.101.0
network 192.168.102.0

passive-interface fa 0/0.101
passive-interface fa 0/0.102
do wr
**R2**
router rip
version 2
no auto-summary

do sh ip ro
network 192.168.11.0
network 192.168.51.0
passive-interface fa 0/0
do wr
далі налаштовую сервер 
потім
**R0**
int fa 0/0.101
ip helper-address 192.168.201.2
do wr
int fa 0/0.102
ip helper-address 192.168.201.2
do wr