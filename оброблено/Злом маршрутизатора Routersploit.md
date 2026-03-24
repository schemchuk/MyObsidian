1  ----------
2 Звязки :  [[вразливості Windows]] , [[Eternal Blue Attack  (eternalblue)]], [[Double pulsar Attack -експлойт Windows]],  [[вразливість Windows--- Bluekeep and EnternalBlue]]

3 Теги : [[Злом маршрутизатора Routersploit]] облікові дані маршрутизатора за замовчуванн
заходжу по посиланню на гітхаб :
routersploit
попадаю на:
https://github.com/threat9/routersploit
копіюю посилання і в терміналі вдкритому на робочому столі набираю:
git clone https://github.com/threat9/routersploit 

а тим часом дивлюся в гіт хабі(зайшов чуть вище) які установочні команди треба мені виконати для калі в терміналі:
установлюю  python3-pip:
sudo apt-get install git python3-pip
переходжу в каталог routersploit

cd routersploit

виконую всі вимоги цього текстового файлу ввівши в термінал:
python3 -m pip install -r requirements.txt
не отримую результату бо хоч цього і нема в уроці але потрібно встановити віртуальне середовище
python3 -m venv venv
Активуйте віртуальне середовище:
source venv/bin/activate
а потім вже запустити інсталяцію
pip install -r requirements.txt
не хоче ще запускати тодлбавляю :

pip install --upgrade setuptools

 далі запускаю сам інструмент Routersploit:

python3 rsf.py

щоб не їбстися кожного разу з запуском Routersploit в вірт середовищі створюю **аліас для запуску Routersploit** :

alias routersploit="source /home/kali/Desktop/routersploit/venv/bin/activate && python3 /home/kali/Desktop/routersploit/rsf.py"

## запуск Routersploit

routersploit це аліас для запуску повинен працювати з будь якого місця в системі:
routersploit

## робота з Routersploit
коли зайти в Routersploit ми побачимо подібну до метасплойту консоль і методи роботи в ній схожі те ж.
можна подивитись всі чотири сканери який використовує Routersploit:
search scanners
будемо зараз використовувати autopwn
і шукати експлойти:
use scanners/autopwn
потім можна подивитися параметри :
show options
і побачити що треба ввести параметри ІР . щоб перевірити ІР адресу маршрутизатора вводимо в **НОВОМУ** терміналі:
netstat -nr
вводимо ІРі;
set target 192.168.1.0
і запускаємо:
run
зараз ми не наблюдаємо + (плюса у виводі роботи) :
[-] 192.168.1.0 Could not confirm any vulnerablity
але оця хуйня недостовірна і її потрібно перевірити:
[-] 192.168.1.0 Could not find default credentials( Не вдалося знайти облікові дані за умовчанням)





кіно тут:
https://www.youtube.com/watch?v=Z-JLJLTqh2A&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=58
