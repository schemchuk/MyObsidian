1   -----------Cisko

2   Связи:  [[налаштування статичного маршруту]]
3   Теги:
1. роблю вссі необхідні підключення(компи, комутатор, маршрутизатор)
на комутаторі заходжу в режим глобальної конфігурації 
enable
conf t
задаю імя хоста
hostname SW1
режим ігнорування неправильно введених команд
no ip domain-lookup
задаю ІР домен
ip domain name AdminSW1
do wr
2. Задаю ІР адресу комутатору
[[VLAN]] 101
ex
interface vlan 101
ip address 192.168.100.254 255.255.255.0
ex
3. Додаю всі порти комутатора в інтерфейс vlan 101
interface range fastEthernet 0/1 -24
switchport mode access
switchport access vlan 101
ex
4. створюю імя користувача і пароль
username AdminSW1 password 123
service password-encryption
5. створюю пароль доступу до привілейованого режиму
enable secret 123456
do wr
6. налаштовую ключ SSH
ip ssh version 2
crypto key generate rsa
512

line vty 0 15
login local
transport input ssh
logging synchronous 
exec-timeout 5
do wr
6. заходжу в командну стрічку через декстоп (з любого компа) і проводжу налаштування
ssh -l AdminSW1 192.168.100.254
спочатку заходжу в режим глобальної конфігурації
enable
conf t
line console 0
login local
logging synchronous
exec-timeout 5
do wr
7. Підключаю консольний кабель до комутатора(синій)
заходжу в термінал і можу авторизовуватися також а потім отримати доступ
