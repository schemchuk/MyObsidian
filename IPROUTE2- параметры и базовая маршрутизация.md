root1   -----------
2   Связи: linux линукс    , linux ,[[Розмежування SU i SUDO]]  [[Системи безпеки  DAC, MAC, SeLinux, AppArmor]]
3   Теги: , [[IPROUTE2- параметры и базовая маршрутизация]]

IPROUTE2 утиліта для роботи з мережею
структура 
ір опції обєкт команда
 подивитись шнтерфейси:
 ip link show
сортувати по устройству
ip link show enp0s3






#### конфігурація
ір link set  устройство параметр значення
-**виключити устройство enp0s3**
sudo ip link set enp0s3 down
-**включити устройство enp0s3** 
sudo ip link set enp0s3 up
-**поміняти розміз кадру** (mtu)
sudo ip link set enp0s3 mtu 1000
-**поміняти мак адресу**:
  виключити устройство enp0s3
sudo ip link set enp0s3 down
sudo ip link set  address 08:00:27:b1:or:cs
   -включити устройство enp0s3 
sudo ip link set enp0s3 up

-**подивитись ір адресу**
ip a
-**присвоїти ще якусь ір адресу** 
 sudo ip a add 192.168.1.222/24 dev enp0s3

---
title: IPROUTE2 — повний швидкий довідник (cheatsheet)
tags: [linux, networking, iproute2, sysadmin, мережа, команди]
created: 2025-10-01
updated: 2026-02-06
---

# IPROUTE2 — повний швидкий довідник (cheatsheet)

Сучасна заміна ifconfig, route, netstat, arp, brctl тощо.  
Працює без legacy-інструментів.

**Загальна структура**  
ip [ОПЦІЇ] ОБ'ЄКТ [КОМАНДА] [ПАРАМЕТРИ]

Основні об’єкти та скорочення:  
- link   / l     — інтерфейси (L2)  
- address / addr / a — IP-адреси  
- route   / r     — маршрути  
- rule          — правила маршрутизації  
- neigh   / n     — сусіди (ARP/NDP)  
- netns         — мережеві namespaces  

Популярні опції:  
-c    кольори  
-br   короткий вивід  
-d    деталі  
-s    статистика  
-4/-6 тільки IPv4/IPv6  


## 1. Інтерфейси (link / l)

ip link show                          # показати всі мережеві інтерфейси
ip l                                  # короткий синонім ip link show
ip -br l                              # максимально коротко + кольори (найзручніше щодня)
ip l show enp0s3                      # показати інформацію тільки про інтерфейс enp0s3
ip -d l show enp0s3                   # детальна інформація (mtu, qlen, driver, state, promisc тощо)
ip -s l show enp0s3                   # показати статистику rx/tx (пакети, байти, помилки, дропи)

sudo ip link set enp0s3 up            # підняти інтерфейс (включити)
sudo ip link set enp0s3 down          # вимкнути інтерфейс
sudo ip link set enp0s3 mtu 9000      # змінити MTU інтерфейсу
sudo ip link set enp0s3 address 0a:11:22:33:44:55   # змінити MAC-адресу
sudo ip link set enp0s3 name lan0     # перейменувати інтерфейс

## 2. IP-адреси (address / addr / a)

ip a                                  # показати всі інтерфейси + ip-адреси
ip -br a                              # коротко + кольори (найзручніше)
ip a show enp0s3                      # показати тільки ip-адреси інтерфейсу enp0s3

sudo ip a add 192.168.77.33/24 dev enp0s3     # додати ip-адресу
sudo ip a add 10.55.6.11/27 dev enp0s3        # додати адресу з іншою маскою
sudo ip a add 192.168.77.200/24 dev enp0s3    # додати ще одну адресу на той самий інтерфейс

sudo ip a del 192.168.77.33/24 dev enp0s3     # видалити конкретну адресу
sudo ip addr flush dev enp0s3                 # видалити ВСІ ip-адреси з інтерфейсу

## 3. Маршрути (route / r)

ip r                                  # показати таблицю маршрутизації
ip -br r                              # коротко + кольори

sudo ip route add default via 192.168.77.1 dev enp0s3          # додати шлюз за замовчуванням
sudo ip route add 10.10.0.0/16 via 192.168.77.254 dev enp0s3   # додати маршрут до мережі
sudo ip route add 172.16.0.0/16 via 10.0.0.1 metric 30 dev eth1  # маршрут з метрикою

sudo ip route replace default via 10.55.0.1 dev enp0s3         # замінити існуючий default маршрут
sudo ip route del 10.10.0.0/16                                 # видалити маршрут
sudo ip route flush table main                                 # видалити всі маршрути з основної таблиці (дуже обережно!)

## 4. Сусіди (neigh / n) — ARP / NDP

ip n                                  # показати ARP-таблицю (IPv4 сусіди)
ip -6 n                               # показати таблицю сусідів IPv6 (NDP)

sudo ip neigh del 192.168.77.55 dev enp0s3    # видалити конкретний запис з ARP-таблиці
sudo ip neigh flush all                       # очистити всю ARP-таблицю

## 5. Повний приклад підняття інтерфейсу вручну

sudo ip link set enp0s3 down
sudo ip link set enp0s3 mtu 1500
sudo ip addr flush dev enp0s3
sudo ip addr add 192.168.88.77/24 dev enp0s3
sudo ip route add default via 192.168.88.1 dev enp0s3
sudo ip link set enp0s3 up

## 6. Швидкі однорядкові трюки

ip a a 192.168.55.3/24 dev eth1           # швидко додати адресу (a a = address add)
ip r add default via 10.0.0.1 dev eth0    # швидко додати default маршрут
ip -c a                                   # кольоровий вивід адрес (кольори)
ip -d l                                   # детальний вивід інтерфейсів
ip -s link                                # статистика по всіх інтерфейсах
watch -n 1 ip -br a                       # моніторинг змін ip-адрес кожну секунду
ip link set lo multicast on               # увімкнути multicast на loopback
ip netns list                             # показати список мережевих просторів імен

## 7. Важливе

• Усі зміни через ip тимчасові — після перезавантаження зникають
• Постійна конфігурація: systemd-networkd / NetworkManager (nmcli) / netplan
• Завжди вказуй dev <інтерфейс> — менше шансів помилитися
• Скорочення працюють майже всі: ip a a = ip addr add, ip r = ip route тощо