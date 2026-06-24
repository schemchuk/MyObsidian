---
title: "пошук уязвимостей вразливостей , скрипти nmap"
category: "networking"
tags: ['проникнення', 'вразливостей', 'share', 'scripts', 'сканування']
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
2 Звязки : [[створення інструменту тестування на проникнення]] , [[сканування]], [[інструмент NMAP]]
3 Теги :[[пошук уязвимостей вразливостей , скрипти nmap]]

## в калі лінукс є цілий розділ із скриптами [[nmap]]
#### заходимо cd /usr/share/nmap/scripts/

cd /usr/share/nmap/scripts/
їх там дуже багато 
варто зайти на офіційну сторінку 
https://nmap.org/man/ru/
там можна знайти групи скриптів для досягнення якоїсь цілі.
в групі даються імена скриптів для використання 
## запускаю групу скриптів для аутентифікації
sudo nmap --script auth 192.168.0.195 -sS
отримую крім основної інформації по відкритих портах що один скрипт знайшов можливість анонімного входу

21/tcp   open  ftp
>>|_ftp-anon: Anonymous FTP login allowed (FTP code 230)

для цього порта :
3306/tcp open  mysql
|_mysql-empty-password: ERROR: Script execution failed (use -d to debug)
виведено шнформацію що доступ до баз mysql без паролю

а тут ми бачимо що до томкату можна підключитися за допомогою ІР адреси і номеру порту:
>>8180/tcp open  unknown
| [[HTTP]]-default-accounts: 
|   [Apache Tomcat] at /manager/html/
|     tomcat:tomcat
|   [Apache Tomcat Host Manager] at /host-manager/html/
|_    tomcat:tomcat
MAC Address: 08:00:27:A9:2A:94 (Oracle VirtualBox virtual NIC)

ось як треба зробити в браузері :

http://192.168.0.195:8180
це офіційна сторінка апаче-томкат 
#### і якщо зайти в розділ адміністратора , тут ми маємо вказати tomcat як імя та як пароль
## то ми заходимо як адміністратор. це знайдена вразливість системи

## перевірка на шкодоносні програми 
sudo nmap --script malware 192.168.0.195 -sS -F
це поки не дало ніякого результату для першої сотні портів-F_

## використання банерів
sudo nmap --script banner 192.168.0.195 -sS -F 
 ми отримуємо банери з версіями 
 21/tcp   open  ftp
|_banner: 220 (vsFTPd 2.3.4)
-----------
22/tcp   open  ssh
|_banner: SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
---------
### хоча і не можливо прочитати але потім побачу що порт telnet
є одним з найпростіших 
23/tcp   open  telnet
|_banner: \xFF\xFD\x18\xFF\xFD \xFF\xFD#\xFF\xFD'
-------

## ще одна група [[сканування]] exploit  
скрипти якої направленні на активне використання уязвимості
sudo nmap --script exploit  192.168.0.195 -sS -F

ось вразливості які це сканування виявило :
VULNERABLE:
|   vsFTPd version 2.3.4 backdoor

IDs:  BID:48539  CVE:CVE-2011-2523
вразливість: CVE-2011-2523

## запуск одиночного скрипта 
sudo nmap --script ftp-anon.nse exploit  192.168.0.195 
виявило можливість анонімного входу 
21/tcp   open  ftp
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
щоб анонімно підключитись вводимо назву скрипта та ІР цільової машини:
ftp 192.168.0.195
потім вводимо  імя довільне i довільний пароль

не дивлячись на написи я в системі і можу ввести help для того щоб побачити доступні команди
