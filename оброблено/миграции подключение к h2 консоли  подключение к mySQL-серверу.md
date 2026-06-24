---
title: "миграции подключение к h2 консоли  подключение к mySQL-серверу"
category: "java_spring"
tags: ['mysql', 'databasechangeloglock', 'удаление', 'серверу', 'введите']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---


Введите команду для подключения к MySQL серверу. Используйте ваш логин и пароль MySQL:

mysql -u root -p

USE url_shortener_db;
Затем выполните удаление таблиц:
DROP TABLE IF EXISTS DATABASECHANGELOG;
DROP TABLE IF EXISTS DATABASECHANGELOGLOCK;

очистить состояние Liquibase и позволить ему заново применить изменения,
USE url_shortener_db;
DROP TABLE IF EXISTS DATABASECHANGELOG;
DROP TABLE IF EXISTS DATABASECHANGELOGLOCK;
 
## подключение к h2 консоли 

етот класс позволяет подключится к консоли h2 из приложения. 
package de.telran.urlshortener;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class H2ConsoleApplication {

    public static void main(String[] args) {
        SpringApplication.run(H2ConsoleApplication.class, args);
    }
}

dropdb имя_вашей_базы_данных

