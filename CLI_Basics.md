# CLI Basics

**Тема:** Основи командного рядка (CLI) в Linux  
**Програма:** Junior Systemadministrator  
**Дата:** 2025-07-25  
**Сесія:** Заняття 1 (Тиждень 1)  
**Пов’язані теми:** Bash Scripting, Linux Permissions, File System Structure

---

## 🎯 Мета заняття

Опанувати базові команди Linux CLI, які використовуються для:
- навігації по файловій системі
- створення, копіювання, видалення файлів
- роботи з редактором `vi`
- пошуку та перегляду інформації
- запуску простого скрипта

---

## 🔹 Основні команди CLI

| Команда | Призначення |
|--------|-------------|
| `pwd` | показати поточний каталог |
| `ls -l` | показати вміст з деталями |
| `cd <dir>` | перейти в каталог |
| `mkdir <dir>` | створити каталог |
| `touch <file>` | створити порожній файл |
| `cp <src> <dst>` | скопіювати файл |
| `mv <src> <dst>` | перемістити або перейменувати файл |
| `rm <file>` | видалити файл |
| `cat <file>` | переглянути вміст файлу |
| `vi <file>` | редагувати файл у vi |
| `find . -name "*.txt"` | знайти всі .txt файли |
| `grep "text" file.txt` | знайти "text" у файлі |
| `wc -l file.txt` | підрахувати кількість рядків |
| `head -n 10` | вивести перші 10 рядків |
| `tail -n 10` | останні 10 рядків |

---

## 🧰 Приклад практичного використання

```bash
# створення робочого каталогу
mkdir testdir
cd testdir

# створення файлу
touch file1.txt

# редагування файлу у vi
vi file1.txt
# Ввести текст, зберегти: Esc → :wq

# копіювання та перейменування
cp file1.txt copy.txt
mv copy.txt moved.txt

# видалення файлу
rm moved.txt

# пошук усіх .txt файлів
find . -name "*.txt"

# перегляд вмісту
cat file1.txt
⚙️ Створення bash-скрипта
vi hello.sh
Встав у файл:
#!/bin/bash
echo "Привіт, $USER! Сьогодні $(date)"
Далі зроби файл виконуваним і запусти:
chmod +x hello.sh
./hello.sh
🧠 Німецька технічна лексика
🇩🇪 Німецьке слово/вираз	🇺🇦 Переклад	🧠 Приклад	🇺🇦 Переклад прикладу
das Verzeichnis	каталог	Wechsle das Verzeichnis mit cd.	Перейди до каталогу за допомогою cd.
die Datei	файл	Erstelle eine neue Datei mit touch.	Створи новий файл за допомогою touch.
der Benutzer	користувач	Der Benutzer kann das Skript nicht ausführen.	Користувач не може виконати скрипт.
der Befehl	команда	Mit dem Befehl ls siehst du alle Dateien.	За допомогою команди ls ти бачиш усі файли.
bearbeiten	редагувати	Bearbeite die Datei mit vi.	Редагуй файл за допомогою vi.
löschen	видаляти	Lösche die Datei mit rm.	Видали файл командою rm.
verschieben	переміщати	Verschiebe die Datei mit mv.	Перемісти файл командою mv.
anzeigen	відображати	Zeige den Inhalt mit cat an.	Виведи вміст файлу через cat.
ausführen	виконувати	Führe das Skript mit ./skript.sh aus.	Запусти скрипт командою ./skript.sh.

🔗 Пов’язані теми
Bash Scripting

Linux Permissions

File System Structure

German for Sysadmins


