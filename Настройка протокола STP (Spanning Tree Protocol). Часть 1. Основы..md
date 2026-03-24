
1   -----------
2   Связи:[[порівняння моделі OSI (7 рівнів) та TCP IP (4 рівні)]]
3   Теги:
kino https://www.youtube.com/watch?v=Er0bAPcTPog

щоб подивитися на комутаторі трафік STP
en 
sh spanning-tree
щоб назначити комутатор **SW3** в якості кореневого
в режимі гл. конф
подивитися налашт влан комутатора do sh vl br
далі назначаємо свіч3 кореневим
spanning-tree [[VLAN]] 1 root primary
do wr
дати цьому комунатору найвищий пріоритет:
spanning-tree vlan 1 priority 0
do wr
пріоритети **рекомендується** задавати всім комутаторам вручну.

**SW1**
spanning-tree vlan 1 priority 4096 коли набираєш неправильний пріоритет то дається підказка 
do wr
**SW2**
spanning-tree vlan 1 priority 8192 коли набираєш неправильний пріоритет то дається підказка 
do wr
**SW0**
spanning-tree vlan 1 priority 12288 коли набираєш неправильний пріоритет то дається підказка 
do wr

# STP (Spanning Tree Protocol) для нескольких VLAN, Rapid PVST Часть 2
 kino https://www.youtube.com/watch?v=NEyBxcrqSgk
налаштування компютерів стандартне
**R0**
після стандартних
int fa 0/0
no sh
int fa 0/0.101
encapsulation dot1Q 101
ip address 192.168.101.1 255.255.255.0
int fa 0/0.102
encapsulation dot1Q 102
ip address 192.168.102.1 255.255.255.0

int fa 0/0.103
encapsulation dot1Q 103
ip address 192.168.103.1 255.255.255.0
do wr
на **SW1** буде запущено VTP сервер
стандартні настройки далі:
vlan 100
exit
vlan 101
exit
vlan 102
exit
vlan 103
exit
do wr
## всі порти будуть у стані trunk
interface range fa 0/21 - 24
switchport mode trunk
switchport trunk native vlan 100
do wr
запуск VTP  сервера на комутаторі SW1
exit
vtp mode server
vtp domain SW1
vtp password 123
do wr
комутатори **SW0 SW2 SW3** будуть **vtp-клієнтами** їхні **port fa/0/24** ,будуть знаходитися в стані **trunk** а **port fa/0/1** **port fa/0/2**
будуть розприділені по vlan
**SW0 SW2 SW3**
стандартні настройки,  далі робиться на кожному свічі однаково:
vtp mode client
vtp domain SW1
vtp password 123
do wr
do sh vl br
int fa 0/24
switchport mode trunk
switchport trunk nanive vlan 100   (стандартно для всіх fa 0/24) 
int fa 0/1
switchport mode acces 
switchport acces vlan 101 (влани розприділяються відповідно схеми)
int fa 0/2
switchport mode acces 
switchport acces vlan 102  (влани розприділяються відповідно схеми)
do wr
do sh vl br
 щоб побачити роботу протоколу **STP** організовую додаткові лінки **fa 0/10 fa 0/11**  між комутаторами **SW0->SW2->SW3**
 після чого потрібно зайти на комутатори і нові порти добавити в **trunk**
 **SW0**
 int fa 0/10
 switchport mode trunk
 switchport trunk native vlan 100
 do wr
 **SW2**
 int range  fa 0/10-11
  switchport mode trunk
 switchport trunk native vlan 100
 do wr
 **SW3**
 int fa 0/11
 switchport mode trunk
 switchport trunk native vlan 100
 do wr 
 ---------------
 щоб визначити кореневий комутатор дивимося STP процеси
 sh spanning-tree
 
 # **зроблю комутатор SW1 кореневим**
 spanning-tree vlan 1 root primary
 spanning-tree vlan 100 root primary
 spanning-tree vlan 101 root primary
 spanning-tree vlan 102 root primary
 spanning-tree vlan 103 root primary
 do wr
 потім по кожному **vlan** потрібно розставити пріоритети в рамках **кожного** комутатора
далі на **SW1**
spanning-tree vlan 1 priority 0  **найвищий**
spanning-tree vlan 100 priority 0  **найвищий**
spanning-tree vlan 101 priority 0  **найвищий**
spanning-tree vlan 102 priority 0  **найвищий**
spanning-tree vlan 103 priority 0  **найвищий**
do wr

**SW0**
spanning-tree vlan 1 priority 4096  (цифри брати з підказки)
spanning-tree vlan 100 priority 4096
spanning-tree vlan 101 priority 4096
spanning-tree vlan 102 priority 4096
spanning-tree vlan 103 priority    4096
do wr
**SW2**
spanning-tree vlan 1 priority 8192 (цифри брати з підказки)
spanning-tree vlan 100 priority 8192
spanning-tree vlan 101 priority 8192
spanning-tree vlan 102 priority 8192
spanning-tree vlan 103 priority    8192
do wr
**SW3**
spanning-tree vlan 1 priority 12288   (цифри брати з підказки)
spanning-tree vlan 100 priority 12288
spanning-tree vlan 101 priority 12288
spanning-tree vlan 102 priority 12288
spanning-tree vlan 103 priority   12288
do wr

#### щоб пришвидшити роботу потрібно зайти в режим протоколу STP (Spanning Tree Protocol) **rapid-pvst**

**SW1**
spanning-tree mode rapid-pvst
do wr
інші налаштування непотрібно міняти

### аналогічні дії на інших комутаторах

**SW0, SW2, SW3**
spanning-tree mode rapid-pvst
do wr





