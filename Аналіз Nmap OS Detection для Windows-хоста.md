1   -----------
2   Связи: [[Повний план пентест-сканування Windows-хоста з Nmap]]
3   Теги: [[Аналіз Nmap OS Detection для Windows-хоста]]
# Аналіз [[nmap]] OS Detection для Windows-хоста

## Вихідні дані [[сканування]]
```text
All 1000 scanned ports on DESKTOP-6I7CGKF.localdomain (192.168.1.18) are in ignored states.
Not shown: 1000 filtered tcp ports (no-response)
Too many fingerprints match this host to give specific OS details
Network Distance: 1 hop
MAC Address: B8:1E:A4:90:52:47 (Liteon Technology)
```

---

## Що це означає

1. **All 1000 scanned ports … are in ignored states**
   - Nmap просканував стандартні 1000 TCP-портів, але усі вони “ignored” → порти фільтруються фаєрволом або не відповідають.

2. **Not shown: 1000 filtered tcp ports (no-response)**
   - Кожен порт **фільтрується** → Nmap не отримав жодної відповіді.

3. **Too many fingerprints match this host to give specific OS details**
   - Nmap не зміг точно визначити ОС через відсутність відкритих портів/сервісів.

4. **Network Distance: 1 hop**
   - Хост знаходиться на **одному стрибку** від скануючого комп'ютера (локальна мережа).

5. **MAC Address**
   - B8:1E:A4:90:52:47 (Liteon Technology) → Windows-десктоп/ноутбук.

---

## Висновок

- OS detection **не спрацював**, бо всі порти **фільтруються**.
- Nmap не отримав жодної інформації про сервіси → OS fingerprinting неможливий.
- Фаєрвол/EDR блокує всі TCP-порти.

---

## Рекомендації

1. **SYN scan всіх портів**:
```bash
nmap -Pn -sS -p- 192.168.1.18
```
- Ігнорування ICMP, пошук відкритих портів, які Nmap не побачив стандартним сканом.

2. **OS detection**
- Працює лише при наявності відкритих портів із сервісами.

3. **Локальна перевірка Windows**
```powershell
systeminfo
```
- Виведе точну версію ОС, архітектуру та патчі.

---

## Подальші кроки

- Якщо мета легальна, можна планувати **обхід фільтрування фаєрволу/EDR**, щоб виявити відкриті порти.
- Наступний крок – поєднати SYN scan, ACK scan та NSE-скрипти для виявлення сервісів.