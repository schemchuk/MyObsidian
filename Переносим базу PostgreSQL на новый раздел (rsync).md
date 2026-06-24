---
title: "Переносим базу PostgreSQL на новый раздел (rsync)"
category: "networking"
tags: ['раздел', 'докер', 'процессы', 'джентельментські', 'переносим']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

2   Связи: [[java  джава]] [[docker докер]] [[гит git hub]] [[работа с гитом]]  [[заначка]], [[проект на докере]] [[виндовс сервер]]  [[ОС реального часу]] [[джентельментські угоди]]  [[Права на файл]] [[процессы]]  [[хак chak]] [[команди лінукс, ключі лінукс]] [[утиліти лінукс]]  , [[сeрвер NetBox]] , [[Переносим базу PostgreSQL на новый раздел (rsync)]] , [[Монтирование раздела под БД (blkid, df-h, lsblk)    Netbox]]    [[сeрвер NetBox]] ,
3   Теги: [[Переносим базу PostgreSQL на новый раздел (rsync)]]
заходжу в  директорію примоннтованого виска sdb1
cd /pstgsql
ставлю базу postgresql
apt install postgresql

	sudo -u postgres psql 
	show data_directory;
\q
systemctl status postgresql
systemctl stop postgresql
## починаю роботу з папками і даними, які потрібно переносити

apt install rsync

	rsync -av /var/lib/postgresql/17 /pstgsql
cd /pstgsql 
ls
появилась папка main
заходжу 
cd //var/lib/postgresql/17
ls
бачу main
переіменовую main.bk
mv main main.bk
заходжу в 

і бачу змонтований диск (lost+found) i main

cd /ets/postgresql/17/main
ls
знаходжу конфігураційний файл postgresql.conf
vim postgresql.conf
і міняю рядок data_directory на 
data_directory = '/pstgsql/main'

systemctl start postgresql
systemctl status postgresql

### взнати де фактично зараз знаходиться місце зберігання бази
sudo -u postgres psql 
show data_directory;
\q