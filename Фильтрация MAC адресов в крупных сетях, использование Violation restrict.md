1   -----------
2   Связи:[[порівняння моделі OSI (7 рівнів) та TCP IP (4 рівні)]]
3   Теги:[[VLAN]]
kino  https://www.youtube.com/watch?v=E4QH61ovmnA
в даній темі буду використовувати лише один комутатор з налаштуваннями Switch0
спочатку налаштовую інтерфуйси хостів(компів)
потім налаштування інтерфейсу маршрутизатора fa 0/0
 потім епісля стандартних настройок  роблю настройку фільтрації мак адрес на комутаторі switch0
 **SW0**
 якщо зайти з привілейованого режиму **en** і подивитися стисок мак адрес інтерфейсу fa 0/21
 show mac-address-table interfaces fa 0/21, **то там вже буде одна мак адреса комутатора Switch**1
 заходжу в режим гл конф
 conf t
 int fa 0/21
 switchport mode access
 sw port-security
 switchport port-security maximum 4 (вказую максимальну кількість портів який може запамятати комутатор SW0 на інтерфейсі fa 0/21)
 прописую решту мак адрес(адреси компів):
 switchport port-security mac-address 0001.96D3.ABE9
 switchport port-security mac-address 0060.4795.7EA0
 switchport port-security mac-address 0002.4AAB.BEC5
краще додати вручну і свіч мак адресу
switchport port-security mac-address 0001.64a2.d518
 do wr
 do sh mac-ad int fa 0/21 *всі мак адреси записані*
 ##щоб ігнорувати наслідки появи порушника , потрібно активувати команду **violation**, яка має три режими:
 - Protect  відключає порушника
 - Restrict буде сформовано SMP пакет з інформацією про порушника
 - Shutdown відключає всю гілку
switchport port-security violation protect
--------------
такі ж налаштування на решті свічів
 **int fa 0/22**
 SW0(config-if)#switchport port-security mac-address 0060.5C7D.3929
SW0(config-if)#switchport port-security mac-address 0060.47C7.3B70
SW0(config-if)#switchport port-security mac-address 0002.4A23.CC56



**int fa 0/23**
SW0(config-if)#switchport port-security mac-address 00E0.F71A.1103
SW0(config-if)#switchport port-security mac-address 0005.5EC5.7EE8
SW0(config-if)#switchport port-security mac-address 00D0.5856.6550
