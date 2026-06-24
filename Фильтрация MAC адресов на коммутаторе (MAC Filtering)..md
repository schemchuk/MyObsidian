---
title: "ще один спосіб фільтрації це задати мак адреси вручну"
category: "networking"
tags: ['watch', 'адресами', 'фільтрація', 'полягає', 'порівняння']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---


1   -----------
2   Связи:[[порівняння моделі OSI (7 рівнів) та TCP IP (4 рівні)]]
3   Теги:[[VLAN]]
kino https://www.youtube.com/watch?v=QXAf2WYf8gs

фільтрація мак адрес полягає в тому, що комутаторам відомо з якими мак адресами дозволено працювати
є декілька способів
- заходимо на комутатор switch1 в реж гл конф
ho SW1
int fa 0/1
switchport mode access
switchport port-security
switchport port-security maximum 1  (вказано запамятати 1 мак адресу)
switchport port-security mac-address sticky (вказується запамятати мак адрес компа який перший звернувся)
do wr
провівши тестування на одному компі можна подивитися як працює функція захисту порта
show port-security int fa 0/1
 якщо підключити на цей інтерфейс інший комп з таким же IP адресою, то зєднання не працюватиме.
 щоб полагодити потрібно перепідключити компютер і на комутаторі **SW1**
 int fa 0/1
 shutdown
 no sh
 do wr
### щоб примінити це налаштування для декількох портів за один раз
**SW1**
int range fa 0/2 -3
switchport mode access
switchport port-security
switchport port-security maximum 1  (вказано запамятати 1 мак адресу)
switchport port-security mac-address sticky (вказується запамятати мак адрес компа який перший звернувся)
do wr
 sh port-security int fa 0/2
 щоб повідключати решту портів, які не використовуються на комутаторі свіч1 **SW1**
 int range fa 0/4 - 23
 shutdown
 do wr
# ще один спосіб фільтрації це задати мак адреси вручну
зроблю це на прикладі **SW2**
 int fa 0/1
 switchport mode access
 switchport port-security
 switchport port-security maximum 1 
 switchport port-security mac-address 0090.212A.40B3    задати вручну мак адресу
 do wr
 **щоб усе запрацювало потрібно прогнати ISMP пакет в режимі симуляції** 
 подивитися в привілейованому режимі (команда щоб зайти **en**)
 show port-security int fa 0/1
### iще один спосіб звідки мохна одержати адресу про мак адресу нашого пристрою 
розгляну на прикладі налаштування інтерфейсу int fa 0/2 na SW2
 int fa 0/2
  switchport mode access
 switchport port-security
 switchport port-security maximum 1 
 заходжу в емуляторі ПК-3 у вкладку config -> FastEthernet0 і там можна побачити і скопіювати мак адресу компютера 
 switchport port-security mac-address 00E0.A3C6.80D7    задати вручну мак адресу
 do wr
  **щоб усе запрацювало потрібно прогнати ISMP пакет в режимі симуляції** 
  подивитися в привілейованому режимі (команда щоб зайти **en**)
 show port-security int fa 0/2
  щоб повідключати решту портів, які не використовуються на комутаторі свіч2 **SW2**
 int range fa 0/3 - 23
 shutdown
 do wr