
1   -----------
2   Связи:[[Проэкт группы]] [[проэкт на spring bot]] 
3   Теги: [[Liquibase  Ликибейс]]
статья
https://dev.to/aharmaz/liquibase-for-[[Spring]]-boot-projects-5hf6
dependensies:
<dependency>
			<groupId>org.liquibase</groupId>
			<artifactId>liquibase-core</artifactId>
			<version>4.27.0</version>
		</dependency>

<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
        xmlns="[[HTTP]]://www.liquibase.org/xml/ns/dbchangelog"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog https://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">
    <?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog
        xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog https://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-3.1.xsd">

    <include file="db/migrations/001_schema.sql"/>
    <include file="db/migrations/002_data.sql"/>

</databaseChangeLog>


#MySQL
spring.datasource.url=jdbc:mysql://localhost:3306/library
spring.datasource.username=root
spring.datasource.password=root

spring.[[JPA]].hibernate.ddl-auto=none
spring.jpa.generate-ddl=false

# --- Liquibase ------
spring.liquibase.enabled=true
spring.liquibase.change-log=classpath:/db/db.changelog-master.xml



## кронвыражения статья


https://tproger.ru/translations/guide-to-cron-jobs