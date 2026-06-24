---
title: "Hymbernate"
category: "networking"
tags: ['джава', 'фреймворки', 'mongodb', 'опираются', 'вещи']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи: [[Spring]] [[java  джава]]  SQL [[Hymbernate]]  [[DB]]
3   Теги:  SQL  [[Hymbernate]] MongoDB [[JPA]]



все фреймворки работающие с базами данных Hymbernate опираются на этот низкоуровневый код и оборачивают его в более общие вещи и  в т.ч Hymbernate
который использует [[Spring]] с объектом Object Relation Mapping **ORM**
  когда определенный объект мапится на определенные таблицы в ДВ и соответственно достается на объект



public class JdbcConnectionExample {  
  
    public static void main(String[] args) throws ClassNotFoundException, SQLException {  
        // Class.forName("com.mysql.cj.jdbc.Driver");  
        //Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/world", "root", "123");  
        try (  
                Connection connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/world", "root", "123");  
                Statement statement = connection.createStatement();  
        ) {  
            statement.setFetchSize(5);  
            ResultSet resultSet = statement.executeQuery("select city.name, city.population from city");  
            ResultSetMetaData metaData = resultSet.getMetaData();  
            int columnCount = metaData.getColumnCount();  
//            System.out.println(resultSet.next());  
            while (resultSet.next()) {  
                for (int i = 1; i <= columnCount; i++) {  
                    System.out.print(resultSet.getString(i) + ", ");  
                }  
                System.out.print("\n");  
            }  
        }  
//          resultSet.close();  
//          statement.close();  
//          connection.close();  
    }  
}

## Framework Hymbernate
используется как

- интерфейс [[JPA]] 
Entitties это сущности в  JPA представленные  POJO объекты

- 


для видалення потим import org.springframework.data.jpa.repository.JpaRepository;

###  давать названия методам в классе репозитория
 давать названия методам в классе репозитория
название методов стрингбута в классе репозитория
можно в следовать **подсказкам идеи**, или повыпендриваться:
https://docs.[[Spring]].io/spring-data/jpa/reference/jpa/query-methods.html


## cвязь Java объектов с DB

cвязь Java объектов с DB происходит с помощью **ORM** , даже не с помощю а ORM и есть технология которая связывает 
**O** - Object
**R** - Relational
**M** - Mapping
ORM это связь джава объектов и **записей** в базу данных

**Контекст_персистентности** набор всех объектов сущностей . Каждый из них это запись в базе данных.
для работы с **Persistence Context** используется **Entity Manager** - с которым мы и взаимодействуем




## о борьбе с рекурсиями
https://www.baeldung.com/jackson-bidirectional-relationships-and-infinite-recursion\

Установка двусторонних отношений 
https://medium.com/huawei-developers/database-relationships-in-spring-data-jpa-8d7181f50f60


работа гибернейта 
https://www.baeldung.com/jpa-cascade-types