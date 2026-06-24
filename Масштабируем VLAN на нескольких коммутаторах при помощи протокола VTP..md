---
title: "Масштабируем VLAN на нескольких коммутаторах при помощи протокола VTP."
category: "networking"
tags: ['маршрутизации', 'основы', 'youtube', 'watch', 'помощи']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи:[[Основы конфигурации VLAN. Основы маршрутизации VLAN.]], [[ Масштабируем VLAN на нескольких коммутаторах при помощи протокола VTP.]] , 
3 [[VLAN]]
 kino https://www.youtube.com/watch?v=8grI3KPAQEc
після топології переходжу до налаштування протоколу VTP
**SW0**
роблю стандартні налаштування
далі
vtp mode server
vtp domain SW0
vtp password 123
do wr
далі створюю [[VLAN]] -u 
vlan 100
name TrunkVLAN
exit
vlan 101
name Dep101
exit
vlan 102
name Dep102
exit
vlan 103
name Dep103
exit
vlan 104
name Dep104
do wr
переводжу порти 22, 23, 24 у стан **trunk**
interface range fastEthernet 0/22-24
switchport mode trunk
switchport trunk native vlan 100
do wr
подивитися на vlan -u
do sh vl br
**SW1.1**
vtp mode client
vtp domain SW0
vtp password 123
do wr
do sh vl br
переводжу порти 22, 23, 24 у стан **trunk**
interface range fastEthernet 0/22-24
switchport trunk native vlan 100
do wr
**SW1.2**
vtp mode client
vtp domain SW0
vtp password 123
do wr
do sh vl br
переводжу порти 22, 23, 24 у стан **trunk**
interface range fastEthernet 0/22-24
switchport trunk native vlan 100
do wr
далі настроюю комутатори
**SW2.1  SW2.2 SW2.3 SW2.4**
vtp mode client
vtp domain SW0
vtp password 123

int fa 0/24
switchport mode trunk
switchport trunk native vlan 100
exit
int fa 0/1
switchport mode access
switchport access vlan 101
exit
int fa 0/2
switchport mode access
switchport access vlan 101
do wr
do sh vl br
далі приступаю до налаштуваннь маршрутизаторів
**R2**
int fa 0/0
no sh
створюю підінтерфейси
int fa 0/0.101
encapsulation dot1Q 101
ip address 192.168.101.1 255.255.255.0
do wr
int fa 0/0.102
encapsulation dot1Q 102
ip address 192.168.102.1 255.255.255.0
do wr
і так решта два
exit
int fa 0/1
no sh
ip address 10.1.101.1 255.255.255.252
do wr
**R1**
стандартно налаштовую і задаю адреси інтерфейсів
запускаю протокол **OSPF**
**R2**
router ospf 2
router-id 2.2.2.2
do sh ip ro
passive-interface fa 0/0.101
passive-interface fa 0/0.102
passive-interface fa 0/0.103
passive-interface fa 0/0.104

network 192.168.101.0 0.0.0.255 area 0
network 192.168.102.0 0.0.0.255 area 0
network 192.168.103.0 0.0.0.255 area 0
network 192.168.104.0 0.0.0.255 area 0
network 192.168.101.0 0.0.0.255 area 0
do wr
**R1**
router ospf 1
router-id 1.1.1.1
do sh ip ro
passive-interface fa 0/0
network 10.1.101.0 0.0.0.3 area 0
network 192.168.200.0 0.0.0.255 area 0
do wr










