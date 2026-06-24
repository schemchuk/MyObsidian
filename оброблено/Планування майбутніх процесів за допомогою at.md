---
title: "Планування майбутніх процесів за допомогою at"
category: "linux"
tags: ['якийсь', 'планування', 'виконання', 'потрібно', 'використовувати']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

 
1   -----------
2   Связи: [[робота з процесами 1|робота з процесами 1]] , [[робота з файлами]]
3   Теги:[[ Планування майбутніх процесів за допомогою at]]Припустімо, вам потрібно виконати завдання в якийсь конкретний день колись у майбутньому. Однак ви знаєте, що в цей день ви будете далеко від машини. Як ви виконаєте завдання?  Ви можете використовувати утиліту **at** для виконання будь-якої неінтерактивної команди в указаний час, 

1. тут я посилаю тестовий (Test) емейл на свою почту :
sendemail -f shemchukaga@gmail.com -t shemchukaga@gmail.com -u "Тест" -m "Перевірка" -a /home/woshe/Downloads/image.png -s smtp.gmail.com:587 -xu shemchukaga@gmail.com -xp "xonn dbas vdec csfc" -o tls=yes
 2. послати всі документи пдф з папки /home/woshe/Downloads на мою електронну адресу через 3 хвилини . для цього створюю скрипт : **send_pdfs.sh**  в ньому в текстовому редакторі:
 

#!/bin/bash

**Знайти всі PDF-файли в папці Downloads**
FILES=$(find /home/woshe/Downloads -type f -name "*.pdf")

**Перевірка, чи є PDF-файли**
if [ -z "$FILES" ]; then
  echo "Немає PDF-файлів для відправки."
  exit 1
fi

**Виконати команду для відправки email з усіма знайденими файлами**
sendemail -f shemchukaga@gmail.com -t shemchukaga@gmail.com -u "Тест: всі PDF файли" -m "Ось всі PDF файли з вашої папки Downloads" -s smtp.gmail.com:587 -xu shemchukaga@gmail.com -xp "xonn dbas vdec csfc" -o tls=yes $(for file in $FILES; do echo -n "-a $file "; done)

**далі надати права на запуск**
chmod +x send_pdfs.sh 
**потім Відправити команду на виконання через 3 хвилини:**
echo "/path/to/send_pdfs.sh" | at now + 3 minutes