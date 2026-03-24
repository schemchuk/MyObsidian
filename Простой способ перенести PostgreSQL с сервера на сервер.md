2   Связи: [[java  джава]] [[docker докер]] [[гит git hub]] [[работа с гитом]]  [[заначка]], [[проект на докере]] [[виндовс сервер]]  [[ОС реального часу]] [[джентельментські угоди]]  [[Права на файл]] [[процессы]]  [[хак chak]] [[команди лінукс, ключі лінукс]] [[утиліти лінукс]]  , [[сeрвер NetBox]], [[Монтирование раздела под БД (blkid, df-h, lsblk)    Netbox]], [[Работаем с данными внутри PostgreSQL из консоли.]]
3   Теги: [[Простой способ перенести PostgreSQL с сервера на сервер]]

вхщджу в машину "Зозділи клоновані" під рутом.

далі входжу як користувач postgres
 sudo su postgres
 psgl
 \l
 \q
 psql --username heroadmin --passvord --host localhost superheroes
 \dt
 SELECT** from herolist;
 \q
Треба знати що домашня директорія для користувача postgres
cd
pwd
/var/lib/postgresql
 i сюди впаде бекап після виконання команди
 pg_dumpall > ./backup.bak
 ls 
 бачу файл backup.bak
задача перенести це на інший хост (копіюю в моїй лабораторії NETBOX і створюю клон з іменем NewPostgreSGL_SERVER) 
 задача перенести це на інший хост
 NewPostgreSGL_SERVER

## на хості  NewPostgreSGL_SERVER
ставлю
apt install -y sudo openssh-server postgresql
ip a
взнаю ІР сервер машини( 192.168.1.75)
 ### і переходжу на машину "розділи клоновані"
знов ставлю 
apt install -y sudo openssh-server 
якщо я не користувач postgres
то зайти на машині ним:
 sudo su postgres
 psgl
далі 
scp backup.bak lessons@192.168.1.75:/home/lessons           (не користувачу руту, а користувачу lessons)
підтверджую
yes
і вводжу пароль користувача lessons
переходжу на машину NewPostgreSGL_SERVER
працюю рутом
cd /home/lessons
ls
і дійсно бачу перенесену папку
backup.bak
cd
перевіряю що є з баз на цій машині
заходжу в користувача postgres
sudo su postgres
psql
\l
і бачу лише бази, створені за замовчуванням
\q
переходжу в користувачf postgres вийшовши з баз даних
\q
добавляю дані із файлу бекапу? який находиться в /home/lessons
psql -f backup.bak postgres
все перенеслось!!!
заходжу в psql і роблю стандартні дії з перенесеною базою. там перенеслося все включно з правами користувачів і власників
\l
можу зайти користувачем з паролем
 psql --username heroadmin --passvord --host localhost superheroes

 \dt
 SELECT** from herolist;
 \q
