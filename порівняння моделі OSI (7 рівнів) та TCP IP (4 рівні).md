---
title: "OSI ↔ TCP/IP — таблиця відповідностей"
category: "networking"
tags: ['приклади', 'протоколів', 'рівнів', 'vlan', 'рівні']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿

1   -----------
2   Связи:[[VLAN]]
3   Теги:
# OSI ↔ TCP/IP — таблиця відповідностей

| **OSI (7 рівнів)**                 | **TCP/IP (4 рівні)**                      | **Приклади протоколів (англ.)**                                         |
| ---------------------------------- | ----------------------------------------- | ----------------------------------------------------------------------- |
| 7. Application (Прикладний рівень) | Application (Прикладний рівень)           | [[HTTP]], HTTPS, FTP, SMTP, POP3, IMAP, DNS, SNMP, SSH, Telnet              |
| 6. Presentation (Рівень подання)   | Application (Прикладний рівень)           | TLS/SSL, MIME, JPEG, MPEG, Base64                                       |
| 5. Session (Сеансовий рівень)      | Application (Прикладний рівень)           | RPC, NetBIOS, SMB, PPTP                                                 |
| 4. Transport (Транспортний рівень) | Transport (Транспортний рівень)           | TCP, UDP, SCTP                                                          |
| 3. Network (Мережевий рівень)      | Internet (Інтернет-рівень)                | IP (IPv4 / IPv6), ICMP, IGMP, (ARP*, RARP*) **RIP**                     |
| 2. Data Link (Канальний рівень)    | Network Access (Рівень доступу до мережі) | Ethernet (IEEE 802.3), PPP, HDLC, Frame Relay, ATM, Wi-Fi (IEEE 802.11) |
| 1. Physical (Фізичний рівень)      | Network Access (Рівень доступу до мережі) | UTP/STP cables, Fiber optic, Radio (Wi-Fi), DSL, Bluetooth              |


# Короткі пояснення (по кроках)

1. **Що показує таблиця**
    
    - OSI — теоретична модель з 7 рівнями для розділення функцій мережі.
        
    - TCP/IP — практичний стек, який зводить представлення/сеанси в прикладний рівень і поєднує фізичний + канальний в «Network Access».
        
2. **Навіщо потрібна відповідність**
    
    - Допомагає зрозуміти, на якому рівні працює конкретний протокол або інструмент (наприклад, `tcpdump`/`Wireshark` — дають пакетний вигляд на мережевому/канальному рівні; `curl` — прикладний рівень).
        
3. **Де що впливає на безпеку (важливо для пентесту)**
    
    - Прикладні протоколи без шифру (HTTP, FTP, Telnet, POP3 без TLS) легко перехопити. Використовуйте `HTTPS`, `SFTP`/`FTPS`, `SSH`.
        
    - PPTP та RARP вважаються застарілими/ненадійними у контексті безпеки.
        
    - ARP — атакований (ARP spoofing) на локальному сегменті — ця вразливість лежить на межі канального/мережевого рівнів.
        
4. **Примітки по ARP/RARP**
    
    - ARP (Address Resolution Protocol) технічно працює «між» канальним та мережевим рівнями: воно переводить IP → MAC для локальної доставки. У таблиці помічено зірочкою.
        
5. **Короткі визначення (виноски)**
    
    - **OSI** — Open Systems Interconnection (модель із 7 рівнів).
        
    - **TCP/IP** — набір протоколів інтернету; практична модель зі 4 рівнями.
        
    - **HTTP / HTTPS** — HyperText Transfer Protocol (Secure — з TLS).
        
    - **FTP** — File Transfer Protocol (не шифрує: небезпечний без TLS).
        
    - **SMTP / POP3 / IMAP** — поштові протоколи (SMTP — для відправки; POP3/IMAP — для читання).
        
    - **DNS** — Domain Name System (переклад доменів у IP).
        
    - **SNMP** — Simple Network Management Protocol (керування/моніторинг мережі).
        
    - **TLS / SSL** — криптографічні протоколи шифрування для прикладних потоків.
        
    - **RPC / SMB / NetBIOS** — сеансові/файлові/викликові служби (мережевий доступ до ресурсів).
        
    - **TCP** — Transmission Control Protocol (надійний, з’єдн.-орієнтований).
        
    - **UDP** — User Datagram Protocol (ненадійний, без встановлення з’єднання).
        
    - **SCTP** — Stream Control Transmission Protocol (альтернатива TCP для деяких застосунків).
        
    - **IP** — Internet Protocol (маршрутизація пакетів).
        
    - **ICMP** — Internet Control Message Protocol (діагностика, наприклад `ping`).
        
    - **IGMP** — Internet Group Management Protocol (multicast).
        
    - **ARP / RARP** — Address Resolution / Reverse ARP (зв’язок IP ↔ MAC).
        
    - **Ethernet / Wi-Fi / PPP / HDLC / ATM** — технології канального рівня.
        
    - **UTP / Fiber / DSL / Bluetooth** — приклади фізичних середовищ.
        
6. **Короткий практичний мінімум (для лабораторії пентеста)**
    
    - Вміти визначити: на якому рівні працює вразливість (L1–L7).
        
    - ARP spoofing / MITM — L2/L3; IP spoofing / routing — L3; SYN flooding — L4; HTTP injection / RCE — L7.
        
    - Для аналізу трафіку використовуй `Wireshark` (пакети L2–L3), `tcpdump` (CLI), `Burp Suite` (L7 для веб).
        
7. **Попередження про застарілі або сумнівні методи**
    
    - **Telnet, FTP, POP3 без TLS, PPTP** — вживати лише в лабораторії або етапах тестування; не застосовувати в продакшн.
        
    - **RARP** практично не використовується у сучасних мережах.
        
    - Окрім протоколів, звертай увагу на реалізації — старі версії TLS (1.0/1.1) мають вразливості.