---
title: "dto обекты"
category: "java_spring"
tags: ['обекты', 'mabstracn', 'baeldung', 'фреймморк', 'мабстракта']
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
2   Связи: [[проэкт на spring bot]] [[Spring]]
3   Теги:[[dto обекты]]

фреймморк mabstracn

https://www.baeldung.com/mapstruct

для работы мабстракта с ломбоком нужны зависимости

<dependency>
    <groupId>org.mapstruct</groupId>
    <artifactId>mapstruct</artifactId>
    <version>1.5.5.Final</version>
</dependency>


выносятся в отдельные переменые версии мапстракта и ломбока и размещаются ниже версии идеи в помнике:

<mapstruct.version>1.5.5.Final</mapstruct.version>
<lombok.version>1.18.32</lombok.version>

плагины:
<plugin>
    <groupId>org.apache.[[Maven]].plugins</groupId>
    <artifactId>maven-compiler-plugin</artifactId>
    <version>3.8.1</version>
    <configuration>
       <source>8</source>
       <target>8</target>
       <annotationProcessorPaths>
          <path>
             <groupId>org.projectlombok</groupId>
             <artifactId>lombok</artifactId>
             <version>${lombok.version}</version>
          </path>
          <path>
             <groupId>org.projectlombok</groupId>
             <artifactId>lombok-mapstruct-binding</artifactId>
             <version>0.2.0</version>
          </path>
          <path>
             <groupId>org.mapstruct</groupId>
             <artifactId>mapstruct-processor</artifactId>
             <version>${mapstruct.version}</version>
          </path>
       </annotationProcessorPaths>
    </configuration>
</plugin>
### swagger
для генерации автодукоментации по контроллерам используется фреймворк **свагер**

<!--        [[Spring]] doc & Swagger support. URL: [[HTTP]]://localhost:8080/swagger-ui/index.html-->
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.5.0</version>
</dependency>



ссылки на статьи по свагеру
https://www.baeldung.com/spring-rest-openapi-documentation

https://blog.skillfactory.ru/glossary/swagger/
