---
title: "збір електронних листів для домену чи визначеної компанії  theHarvester  і веб сайт hunter.io"
category: "pentesting"
tags: ['назву', 'шукати', 'інформації', 'компанії', 'методи']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

sh
1  ----------
2 Звязки : [[методи збору інформації]]
3 Теги : 
## Інструмент theHarvester 
потребує вказати доменне імя або назву компанії чи сайту
-b ключ який показує де шукати  в даному випадку заданий пошук all(все). за замовчуванням видасть результат 500 пошуків, можна міняти ключом 

theHarvester -d mas.bg.ac.rs -b all
Інструмент theHarvester працює **нестабільно і** може видати дохуя і ніхуя також 
тому **варто** сканувати кілька раз в різні дні

## веб сайт hunter.io

заходимо в браузері в hunter.io
але там треба реєструватися, і бажано платну версію.

можна і навіть потрібно шукати в **github**. можна шукати як конкретний інструмент так і задати в пошуку  : **інстументи пошуку інформаціі гіт-хаб**  по аглицьки **Information Gathering Tools github**
**треба набирати:**
Information Gathering Tools github

сторінка інструменту https://github.com/Tuhinshubhra/RED_HAWK

щоб установити програму в терміналі набираєм git clone і даємо адресу сторінки : 
git clone https://github.com/Tuhinshubhra/RED_HAWK 
 далі заходимо в RED_HAWK  і визначаємо що файл rhawk.php  є файлом запуску. (я не зрозумів як визначати) потім запускаємо файл. Так як це файл php, то запуск так і починається :
 php rhawk.php
після завантаження в терміналі показує що потрібно пофіксити програму :
[!] cURL Module Is Missing! Try 'fix' command OR Install php-curl
[!] DOM Module Is Missing! Try 'fix' command OR Install php-xml
тому вводжу в термінал команду **fix**


## Інструмент шерлок запускається так:
 sherlock  і далі аргументи 
бо я вже його установив 
потім дивимось результати пошуку :
cat vasyapupkin.txt 