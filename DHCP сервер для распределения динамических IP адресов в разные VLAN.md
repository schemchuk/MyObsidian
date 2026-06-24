---
title: "DHCP сервер для распределения динамических IP адресов в разные VLAN"
category: "networking"
tags: ['порівняння', 'моделі', 'youtube', 'watch', 'починаються']
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
kino https://www.youtube.com/watch?v=atou9Ouw_OI

починаються налаштування з комутатора , де створюється 4 [[VLAN]]-и
hostname SW0
vlan 100
vlan 101
vlan 102
vlan 103
int fa 0/1
switchport mode access
switchport access vlan 101

int fa 0/2
switchport mode access
switchport access vlan 102

int fa 0/3
switchport mode access
switchport access vlan 103

int fa 0/24
switchport mode trunk
switchport trunk native vlan 100

do wr
**R0**
hostname R0
int fa 0/0
no sh

int fa 0/0.101
encapsulation dot1Q 101
int fa 0/0.102
encapsulation dot1Q 102
int fa 0/0.103
encapsulation dot1Q 103

int fa 0/0.101
ip address 192.168.101.1 255.255.255.0
int fa 0/0.102
ip address 192.168.102.1 255.255.255.0
int fa 0/0.103
ip address 192.168.103.1 255.255.255.0
do wr

налаштовую інтерфуйс пристрою, де буде запущено DHCP сервер

далі на **R0**
int fa 0/0.101
ip helper-address 192.168.103.10
int fa 0/0.102
ip helper-address 192.168.103.10
do wr
do sh run