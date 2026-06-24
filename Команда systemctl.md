---
title: "Команда systemctl"
category: "networking"
tags: ['dhcp', 'сервера', 'сеpвер', 'linux', 'systemctl']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи: linux линукс    , linux , [[Підняти сервер DHCP]] , [[Підняти сеpвер ssh]]
3   Теги: , [[Команда systemctl]]
синтаксис:
systemctl команда(що робим) обєкт(над чим робимо)

дивлюся статус  сервера ssh
systemctl status sshd 
зупиняю :
systemctl stop sshd
якщо тепер перевірити стаеус то отримую
inaktive (dead)
пробую стартанути:
systemctl start sshd
статус стає активним
active (runing)
 при перезавантаженні служба активна
команди dasable 
         enable   використовуються для вказування службі бути активною чи виключеною після перезавантаження  
systemctl disable sshd
зупиняються два сервіси
sshd.service
ssh.service
reboot (при перезагрузці сервер не працює)
командa start не працює.

роблю 
systemctl enable sshd  - теж не працює

потрібно запустити сервіс ssh
systemctl enable ssh.service 
після перезавантаження статус показує неактивний
але після команди
systemctl start sshd
 сервер запрацює
ще команди:
systemctl list-units виводить **активні** юніти(служби)
systemctl list-units --all    виводить **всі наявні** юніти(служби)

systemctl list-unit-files   перераховує всіх установлених в системі служб і їх стан





