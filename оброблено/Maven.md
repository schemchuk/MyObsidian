---
title: "Maven"
category: "java_spring"
tags: ['сборщик', 'класс', 'нужно', 'писали', 'архива']
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
2   Связи: [[json]]  [[артефакт]]  [[сборщик проекта]] 

3   Теги:  


Диплоймен   

раньше код писали в текстовых файлах которые имели расширение .**java**  
классы нужно было компилировать вручную с расширением .**class**  и только класс с методом **мейн** можно было специальным образом запуститьВ данное время два архива
1. .jar для упаковки и распостранения всех ресурсов , библиотеки, классы, метаданные и т. д.
2. .war предназначены для выполнения в ВЕБ контейнере  
**Сборщик проэкта** это некий скриптовый код 
**Скрипт** это последовательность команд

### выполняемый файл
<!-- выполняемый JAR в maven проекте -->
<build>
	<plugins>
		<plugin>
			<groupId>org.apache.maven.plugins</groupId>
			<artifactId>maven-jar-plugin</artifactId>
			<version>3.3.0</version>
			<configuration>
				<archive>
					<manifest>
						<addClasspath>true</addClasspath>
						<classpathPrefix>lib/</classpathPrefix>
						<mainClass>com.telran.Main</mainClass>
					</manifest>
				</archive>
			</configuration>
		</plugin>
	</plugins>
</build>


mvn help: effective-pom



От Александра для спринг бута депенденси

<dependency>
            <groupId>org.springframework</groupId>
            <artifactId>[[Spring]]-core</artifactId>
            <version>6.1.4</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>6.1.4</version>
        </dependency>


<dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-core</artifactId>
            <version>6.1.4</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>6.1.4</version>
        </dependency>







