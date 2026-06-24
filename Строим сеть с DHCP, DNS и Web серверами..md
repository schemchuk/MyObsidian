---
title: "Строим сеть с DHCP, DNS и Web серверами."
category: "networking"
tags: ['мають', 'порівняння', 'моделі', 'youtube', 'watch']
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
kino https://www.youtube.com/watch?v=DxBO1QFxypI
починаю з налаштування периферійних пристроїв які мають стаціонарні ІР адреси.
далі запускаю влани на комутатрі SW0
**SW0**
стандартні
[[VLAN]] 100
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
sh vl br
далі налаштовуються інтерфейси маршрутизаторів
**R1**
int fa 0/0
no sh

int fa 0/0.101
encapsulation dot1Q 101
ip address 192.168.101.1 255.255.255.0
int fa 0/0.102
encapsulation dot1Q 102
ip address 192.168.101.1 255.255.255.0

int eth 0/0/0
no sh
ip address 10.1.0.2 255.255.255.0
int eth 0/1/0
no sh
ip address 10.1.0.1 255.255.255.0
do wr
**R2**
int fa 0/0
ip address 192.168.1.1 255.255.255.0

int eth 0/1/0
no sh
ip address 10.2.0.2 255.255.255.0
int eth 0/0/0
no sh
ip address 10.3.0.1 255.255.255.0
do wr
**R3**
int fa 0/0
no sh
ip address 192.168.201.1 255.255.255.0
int eth 0/0/0
no sh
ip address 10.3.0.2 255.255.255.0
int eth 0/1/0
no sh
ip address 10.4.0.1 255.255.255.0
do wr
**R4**
int fa 0/0
no sh
ip address 192.168.10.1 255.255.255.0

int eth 0/1/0
no sh
ip address 10.4.0.2 255.255.255.0
int eth 0/0/0
no sh
ip address 10.5.0.1 255.255.255.0
do wr
**R0**
int fa 0/0
no sh
ip address 192.168.150.1 255.255.255.0

int eth 0/1/0
no sh
ip address 10.1.0.1 255.255.255.0
int eth 0/0/0
no sh
ip address 10.5.0.2 255.255.255.0
do wr
 **приступаю до налаштування протоколу RIP**
 **R1** R2 R3 R4 R0
 режим гл конф
 router rip
 version 2
 no auto-summary
 do sh ip ro
 network 10.1.0.0
network 10.2.0.0
network 192.168.101.0
network 192.168.102.0
passive-interface fa 0/0.101
passive-interface fa 0/0.102
do wr
**R2**
 режим гл конф
 router rip
 version 2
 no auto-summary
 do sh ip ro
network 10.2.0.0
network 10.3.0.0
network 192.168.1.0
passive-interface fa 0/0
do wr
**R3**
 режим гл конф
 router rip
 version 2
 no auto-summary
 do sh ip ro
network 10.3.0.0
network 10.4.0.0
network 192.168.201.0
passive-interface fa 0/0
do wr
**R4**
 режим гл конф
 router rip
 version 2
 no auto-summary
 do sh ip ro
network 10.4.0.0
network 10.5.0.0
network 192.168.10.0
passive-interface fa 0/0
do wr
**R0**
 режим гл конф
 router rip
 version 2
 no auto-summary
 do sh ip ro
network 10.1.0.0
network 10.5.0.0
network 192.168.150.0
passive-interface fa 0/0
do wr
подивитися на маршрутизаторах, які таблиці маршрутизації на них сформовані

do sh ip ro
#### налаштування  DHCP сервера
проводяться в вікні пристрою
потім треба донастроїти інтерфейси fa 0/0101 та fa 0/0.102 на R1 вказавши в якості нелпер адрес адресу DHCP сервера 192.168.10.2
**R1**
int fa 0/0.101
ip helper-address 192.168.10.2
int fa 0/0.102
ip helper-address 192.168.10.2
do wr
do sh run
запускаю на компах процес одержання ІР адрес
### Приступаю безпосередньо до налаштування  DNS сервера
 в позиції **name** потрібно вказати доменне імя сервера, по якому будемо до нього звертатися
 в мережі є два таких сервера : 
 1. Web Server2 [[HTTP]]://shop.com 192.168.201.3
 2. Web Server1 http://student.com 192.168.201.2
 вказую імя в полі **name** та ІР адресу в полі **Addres**
 далі нажимаю ADD і переходжу аналогічно до запису другого сервера
 ##### **потрібно доналаштувати веб-сервери**
 
 переходжу на сервер вкладку services -> HTTP
   потрібно підредагувати сторінку index (тицяю edit)
   замість синього колору в гіпертексті ставлю червоний
  замість Cisco Packet Tracer пишу Student Days Corporation
   замість Cisco Packet Tracer пишу Student.com
   save
   таким чином і з другим сервером.