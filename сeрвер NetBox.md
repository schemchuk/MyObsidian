---
title: "сeрвер NetBox"
category: "networking"
tags: ['докер', 'процессы', 'джентельментські', 'ключі', 'сервер']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи: [[java  джава]] [[docker докер]] [[гит git hub]] [[работа с гитом]]  [[заначка]], [[проект на докере]] [[виндовс сервер]]  [[ОС реального часу]] [[джентельментські угоди]]  [[Права на файл]] [[процессы]]  [[хак chak]] [[команди лінукс, ключі лінукс]] [[утиліти лінукс]] 
3   Теги: [[линукс linux]] [[сeрвер NetBox]] 
встановити сервер:
apt update
apt instal postgresql

systemctl start postgresql
systemctl status postgresql

включити при старті щоб розверталася
systemctl enable postgresql


-- 1. Заходимо під postgres (виконується в звичайному терміналі Kali / Linux)
sudo -u postgres psql

-- 2. Всередині psql виконуємо по черзі:

-- Створюємо базу даних
CREATE DATABASE netbox;

-- Створюємо користувача (правильний синтаксис)
CREATE USER netbox WITH PASSWORD '111';

-- Даємо користувачу права власника на базу
ALTER DATABASE netbox OWNER TO netbox;

-- (опціонально) даємо всі привілеї на базу (NetBox цього зазвичай не вимагає, але іноді корисно)
GRANT ALL PRIVILEGES ON DATABASE netbox TO netbox;


отримати доступ 
psql --username netbox --password --host localhost netbox;

перевірити :
\conninfo
/q

 установити REDIS
apt install -y redis-server
перевірити 
redis-cli ping
дає відповідь:
PONG

підвантажую пакети для подальшого розгортання
apt install -y python3 python3-pip python3-venv python3-dev build-essential libxml2-dev libxslt1-dev libffi-dev libpq-dev libssl-dev zlib1g-dev (тут заміст l треба в деяких ставити 1)

pip3 install --upgrade pip ця команда не йде , тому роблю так:

- Якщо venv ще не створено — створи (рекомендую окрему папку для NetBox):
python3 -m venv /opt/netbox-venv
- Активуй venv (найважливіший крок):
source /opt/netbox-venv/bin/activate
(після цього prompt стане (netbox-venv) root@debian:~# або подібне)
- Тепер онови pip уже всередині
venv: pip install --upgrade pip 
- (має пройти без жодних помилок externally-managed)
- Перевір версію pip (має бути 24.x або новіша): 
pip --version
- Встанови wheel (щоб уникнути проблем з компіляцією деяких пакетів):
pip install wheel
- - Перейди в директорію NetBox (якщо не там): cd /opt/netbox
    - Якщо клон зроблено не на v4.5.2 — перевір/перейди на тег: git checkout v4.5.2
    - Перейди в піддиректорію з manage.py: cd netbox
    - Встанови всі залежності (це ключовий крок, може зайняти 5–15 хв): pip install -r requirements.txt
    - Якщо psycopg2 не встановився — додай вручну: pip install psycopg2-binary
    - Створи директорію конфігу (якщо ще немає): mkdir -p netbox/configuration
    - Скопіюй приклад: cp netbox/configuration_example.py netbox/configuration/configuration.py
    - Відкрий файл у vim: vim netbox/configuration/configuration.py
    - У vim внеси/зміни ці рядки (шукай за /ALLOWED_HOSTS тощо, режим вставки i, вихід Esc + :wq): ALLOWED_HOSTS = ['*'] SECRET_KEY = 'твій_рандомний_рядок_тут_мінімум_50_символів' DATABASE = { 'NAME': 'netbox', 'USER': 'netbox', 'PASSWORD': '111', 'HOST': 'localhost', 'PORT': '', 'CONN_MAX_AGE': 300, 'OPTIONS': {}, } REDIS = { 'tasks': { 'HOST': 'localhost', 'PORT': 6379, 'DATABASE': 0, 'SSL': False, }, 'caching': { 'HOST': 'localhost', 'PORT': 6379, 'DATABASE': 1, 'SSL': False, } } DEBUG = True # тільки для лабу
    - Згенеруй SECRET_KEY, якщо немає (можна в іншому терміналі або після :wq): python3 -c "import secrets; print(secrets.token_urlsafe(50))" встав результат у файл

1. - Перевір синтаксис конфігу: 
python3 -m py_compile netbox/configuration/configuration.py (не повинно бути помилок)
    - Виконай міграції: 
    python3 manage.py migrate
перейти в 
cd   /opt/netbox/netbox

    - Створи адміністратора:
python3 manage.py createsuperuser (введи username, email, password)

№№№№№№№№№№№№№№№№№№№№№№№№№№№

    - Збери статичні файли:
    python3 manage.py collectstatic --no-input
    - Запусти тестовий сервер: 
    python3 manage.py runserver 0.0.0.0:8000 --insecure  (в режимі розробника. в простому режимі без --insecure)
    - Перевір у браузері на хості: [[HTTP]]://IP_Debian_VM:8000 Логін — той, що створив
    - Зупини Ctrl+C коли перевіриш
2


Варіант 2: Запуск через gunicorn (рекомендую, стабільніше)

- Активуй venv: source /opt/netbox-venv/bin/activate
- Перейди в директорію: cd /opt/netbox/netbox
- Запусти: gunicorn --pythonpath /opt/netbox/netbox --workers 3 --bind 0.0.0.0:8000 netbox.wsgi
- Відкрий у браузері: [http://192.168.1.174:8000](http://192.168.1.174:8000)
- Зупини: Ctrl+C
№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

## далі працюю НЕ в VENV а просто в терміналі рута

 ###  netbox написано на пітоні і для роботи він потребує HTTP server шлюзового інтерфейсу 
 Джиюнікор розвертається автоматом з нетбоксом
 відредагувати конфігураційний файл:
 cd /opt/netbox/contrib
 перекидаю(копіюю) файл gunikorn.py на директорію вище
 cp gunicorn.py /opt/netbox
### роблю netbox  системним сервісом

cd /opt/netbox/contrib
ls
установлюю  netbox-rq.service  netbox.service як системні сервіси

cp -v netbox-rq.service  netbox.service /etc/systemd/system

обновляю демони:
systemctl daemon-reload
стартую їх(демонів)
systemctl start netbox netbox-rq
добавляю їх в завантажувальні
systemctl enable netbox netbox-rq

перевірити статус

systemctl status netbox netbox-rq
 ### переходжу до налаштування HTTP сервера (конкретно nginx)
 apt install nginx
 systemctl status nginx
 ### роблю доступ до https  з використанням ssl сертифікату (в середині компанії це можливо і не потрібно)
 ssl ключі купляються за гроші.
конкретно тут я бавлюся (і це не потрібно на всіх підпр. купляти ключі) і видаю сам собі самопідписаний ключ
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/netbox.key -out /etc/ssl/certs/netbox.crl 
спитає країну(Country Name)   DE
             (full name)  Munich Germany
             (eq, city) Landshut
             (Organization Name)  Paraska Trust
             (Organszational)  IT
             (Common Name)  BestAdmin
 перевірити ключі 
 сd /etc/ssl/private
 ls
 далі 
 cd /etc/ssl/certs
 ls | grep netbox
## продовжую працювати з ngnx

cd /opt/netbox/contrib
ls
цікавить файл nginx.conf
cp nginx.conf /etc/nginx/sites-available/netbox

cd /etc/nginx/sites-available/
ls
rm default

cd ..
ls
цікавить sites-enabled  потрібно щоб тут було посилання на конфігураційний файл
спочатку в цей конфігураційний фал вношу зміни

cd sites-available
vim netbox
i міняю імя сервера на мій ІР адрес(192.168.1.174)  без ніяких лапок

потрібно створити посилання на цей файл в директорії sites-enabled

ln -s  /etc/nginx/sites-available/netbox /ets/nginx/sites-enabled/netbox

cd ..
cd sites-enabled
ls
rm default
ls -l
залишається netbox, який є посиланням 

рестартувати
systemctl restart nginx
systemctl status nginx