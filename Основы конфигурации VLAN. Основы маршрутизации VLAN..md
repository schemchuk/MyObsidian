
1   -----------
2   Связи:[[VLAN]]
3   Теги: [[Основы конфигурации VLAN. Основы маршрутизации VLAN.]]

kino    https://www.youtube.com/watch?v=D362VgEDtKk

після складання топології 
переходжу до налаштування свіча , зробивши стандартні налаштування переходжу до налаштування [[VLAN]]
vlan 101
name Deportment101
exit
vlan 102
name Deportment102

vlan 100
name VlanTrunk
do wr
exit
приступаю до налаштування інтерфейсів
int fa 0/1
description Dep101 Задаю імя
і вказую до якого **vlan** буде відноситися
switchport mode access
switchport access vlan 101
do wr
exit

---
int fa 0/2
description Dep102 Задаю імя
і вказую до якого **vlan** буде відноситися
switchport mode access
switchport access vlan 102
do wr
exit

----
int fa 0/24
switchport mode trunk
switchport trunk native vlan 100
do wr
exit
exit
sh vlan brief Тодивитися на вілани

активую канал fa 0-24
**R1** роблю стандартні налаштквання заходжу на інтерфейс fa 0/0  і вкл його

fa 0/0
no sh
description InputInterR1 задаю імя
далі створюю підінтерфейси
int fa 0/0.101
int fa 0/0.102
- налаштування інт int fa 0/0.101
int fa 0/0.101
encapsulation dot1Q 101 вказую 
ip address 192.168.101.1 255.255.255.0
do wr
- налаштування інт int fa 0/0.102
int fa 0/0.102
encapsulation dot1Q 102 вказую 
ip address 192.168.102.1 255.255.255.0
do wr
далі просто проводжу доналаштування **R1**  стандартно налаштувавши інтерфейс fa 0/1 10.1.101.1/30
і стандартно налаштувавши **R2** налаштувавши стандартно int fa 0/1 i fa 0/0
запускаю протокол маршрутизації **OSPF**
**R2**
router ospf 2
router-id 2.2.2.2
do sh ip ro
network 10.1.101.0 0.0.0.3 area 0
network 192.168.20.0 0.0.0.255 area 0
інтерфуйс  fa 0/0 оголошую **пасивним**
passive-interface fa 0/0
do wr
**R1**
router ospf 1
router-id 1.1.1.1
passive-interface fa 0/0.101
passive-interface fa 0/0.102
do sh ip ro
network 10.1.101.0 0.0.0.3 area 0
network 192.168.101.0 0.0.0.255 area 0
network 192.168.102.0 0.0.0.255 area 0
do wr

