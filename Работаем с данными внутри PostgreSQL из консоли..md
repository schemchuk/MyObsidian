---
title: "PostgreSQL: створення БД, користувача і таблиці (працюючий мінімум)"
category: "networking"
tags: ['докер', 'процессы', 'джентельментські', 'ключі', 'сeрвер']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

2   Связи: [[java  джава]] [[docker докер]] [[гит git hub]] [[работа с гитом]]  [[заначка]], [[проект на докере]] [[виндовс сервер]]  [[ОС реального часу]] [[джентельментські угоди]]  [[Права на файл]] [[процессы]]  [[хак chak]] [[команди лінукс, ключі лінукс]] [[утиліти лінукс]]  , [[сeрвер NetBox]], [[Монтирование раздела под БД (blkid, df-h, lsblk)    Netbox]]
3   Теги: [[Работаем с данными внутри PostgreSQL из консоли.]]


# PostgreSQL: створення БД, користувача і таблиці (працюючий мінімум)

## Середовище
- ОС: Debian / Kali (VM у VirtualBox)
- СУБД: PostgreSQL 17
- Ролі:
  - `postgres` — суперкористувач PostgreSQL
  - `heroadmin` — користувач для роботи з БД
- База даних: `superheroes`

---

## 1. Вхід у PostgreSQL від імені postgres
**Термінал ОС (bash), root або sudo**
```bash
sudo -u postgres psql
Prompt:

postgres=#
2. Створення бази даних і користувача
psql → користувач postgres

CREATE DATABASE superheroes;
CREATE USER heroadmin WITH PASSWORD 'qwerty';
3. Призначення власника БД
Ключовий крок. Без нього можливі проблеми з CREATE TABLE.

psql → користувач postgres

ALTER DATABASE superheroes OWNER TO heroadmin;
4. Права на schema public
PostgreSQL створює таблиці всередині schema, не напряму в БД.

psql → користувач postgres

\c superheroes
GRANT ALL ON SCHEMA public TO heroadmin;
ALTER SCHEMA public OWNER TO heroadmin;
Вихід:

\q
5. Підключення як heroadmin
Термінал ОС (bash)

psql -U heroadmin -d superheroes -h localhost
Prompt:

superheroes=>
Перевірка підключення:

\conninfo
6. Створення таблиці
psql → користувач heroadmin

CREATE TABLE herolist (
    id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    surname VARCHAR(20),
    age INTEGER
);
Перевірка:

\dt
7. Заповнення таблиці
INSERT INTO herolist (name, surname, age) VALUES
('Тоні', 'Старк', 48),
('Наташа', 'Романова', 35);
8. Перевірка даних
SELECT * FROM herolist;
9. Корисні перевірки (опціонально)
Структура таблиці:

\d herolist
Кількість рядків:

SELECT COUNT(*) FROM herolist;
Очистити таблицю:

TRUNCATE TABLE herolist;