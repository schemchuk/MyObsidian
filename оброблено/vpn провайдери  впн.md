
1   -----------
2   Связи: [[хак chak]]
3   Теги:

# DDoS 2 VPN (Kali Linux)

virtuaka edited this page Mar 20, 2022 · [4 revisions](https://github.com/virtuaka/hacking/wiki/DDoS-2---VPN-(Kali-Linux)/_history)

Відео: [https://youtu.be/7AS1UeB8beI](https://youtu.be/7AS1UeB8beI)

Щоб захиститись і замаскуватись під час здійснення кібератак через інтернет, хакеру потрібен VPN.

# Безкоштовний VPN

[](https://github.com/virtuaka/hacking/wiki/DDoS-2---VPN-(Kali-Linux)#безкоштовний-vpn)

Відкриваємо командний рядок (термінал) в ОС Kali Linux.

//коментар: завантажити список пакунків, які можна встановити на ОС  
`sudo apt-get update`  
//коментар: це інструмент який нам дозволить додати налаштування для нашого ВПН  
`sudo apt install gedit`  
//коментар: встановлюємо OpenVPN  
`sudo apt install openvpn`  
// переходимо в спеціальну папку  
`cd /usr/local/bin`  
//коментар: далі, нам потрібно створити файл з скриптом, який буде запускати VPN  
`sudo gedit autovpn3.sh`  
//коментар: ставляємо текст скрипта звідси - [англомовна версія](https://en.kali.tools/?p=1227) або [російськомовна версія](https://kali.tools/?p=6362)  
//коментар: в рядку №8, змінюємо на наступне  
`country=$1 # empty for any or JP, KR, US, TH, etc.`  
//коментар: зберігаємо файл і закриваємо редактор  
//коментар:кажемо лінуксу, що цей файл можна запускати  
`sudo chmod +x autovpn3.sh`  
//коментар: запускаємо  
`sudo autovpn3.sh`  
//коментар: шукаємо двобуквений код країни тут [https://en.wikipedia.org/wiki/ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2)  
//коментар: запускаємо ВПН для потрібної країни  
`sudo autovpn3.sh RU`  
//коментар: заходимо на [www.whatismyipaddress.com](http://www.whatismyipaddress.com) і перевіряємо чи ВПН працює

# Платний VPN - безкоштовно

[](https://github.com/virtuaka/hacking/wiki/DDoS-2---VPN-(Kali-Linux)#платний-vpn---безкоштовно)

Є можливість скористатися [https://nordvpn.com](https://nordvpn.com)

NordVpn зараз надає безкоштовний vpn для жителів України. Для отримання безкоштовного доступу напишіть їм в чат на сайті або на пошту [support@nordvpn.com](mailto:support@nordvpn.com). Після цього потрібно зробити тест локації (аби пересвідчитись що ви з України).

# Платний VPN

[](https://github.com/virtuaka/hacking/wiki/DDoS-2---VPN-(Kali-Linux)#платний-vpn)

[ExpressVPN - мій реферрал лінк](https://www.expressrefer.com/refer-a-friend/30-days-free?referrer_id=60098478&utm_campaign=referrals&utm_medium=copy_link&utm_source=referral_dashboard) або [Windscribe](https://windscribe.com/guides/linux)

Інструкція для ExpressVPN (також доступна тут: [https://www.expressvpn.com/support/vpn-setup/app-for-linux/](https://www.expressvpn.com/support/vpn-setup/app-for-linux/))

_//коментар: цією командою ми переходимо у папку яка називається Downloads_  
`cd Downloads`  
//коментар: розпаковуємо і встановлюємо завантажений файл (у вас ім'я файлу може бути новіше, тому перевірте)  
`sudo dpkg -i expressvpn_3.19.0.13-1_amd64.deb`  
_//коментар: dpkg - це інструмент, який встановлює програми на лінуксі_  
_//коментар: -і означає інсталювати_  
_//коментар: і потім ми вказуємо звідки власне інсталювати програму (тобто де знаходиться файл встановлювач)_  

_//коментар: активуємо програму_  
`expressvpn activate`  
_//коментар: тут потрібно буде ввести код активації з вашого облікового запису на сайті www.expressvpn.com_  
`expressvpn list all`  
_//коментар: ця команда покаже нам список усіх доступних VPN серверів в усіх країнах, до яких ми можемо підключитись_  
_//коментар: вибираємо код тієї країни, через сервер якої ми будемо працювати - наприклад для білорусі код_ `BY`  
`expressvpn connect by`  
_//коментар: команда щоб побачити статус під’єднання у терміналі_  
`expressvpn status`  
_//коментар: команда щоб від'єднатись від VPN_  
`expressvpn disconnect`

 