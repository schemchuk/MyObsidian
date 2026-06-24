---
title: "Підняти сервер DHCP"
category: "networking"
tags: ['dhcp', 'hostname', 'linux', 'працюю', 'install']
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
2   Связи: linux линукс    , linux
3   Теги: [[Підняти сервер DHCP]]
працюю від рута 
#### задаю імя серверу:
vim /etc/hostname
### Встановлюю програмне забезпечення:
apt install isc-dhcp-server

### редагую вкладку:
vim /etc/default/isc-dhcp-server

!Screenshot 2026-02-01 082533 1.png

далі :  vim /etc/dhcp/dhcpd.conf


!Pasted image 20260201083422.png
 потім :
 vim /etc/network/interfaces 
 !Screenshot 2026-02-01 083913.png