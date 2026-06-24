---
title: "БИН компоненты bean"
category: "java_spring"
tags: ['файлы', 'джава', 'нашего', 'внедрение', 'бины']
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
2   Связи: [[Spring]]   SOLID [[java  джава]]  [[Dependensy ingecten внедрение зависимости]] [[Contekst контекст нашего приложения]] [[конфигурационные файлы бины]] 
3   Теги: [[проэкт на spring bot]] 

БИН компоненты bean это компонент внедрения зависимостей,
объект какого то класса


[[конфигурационные файлы бины]] помечаются аннотацией  @**SpringBootApplication** 
и находятся  в папке **resources**


метод **main** присутствует в проэкте как точка входа и он единственный

## работа с бинами
###  XML бины 
создаем ApplicationContext context = new ClassPathXmlApplicationContext("applicfnionContext.xml");
а потом в папке ресурсес создаем файл applicfnionContext.xml
и в нем пишем бины:
<?xml version="1.0" encoding="UTF-8"?>  
<beans xmlns="[[HTTP]]://www.springframework.org/schema/beans"  
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/[[Spring]]-beans.xsd">  
  
    <bean name="france" class="de.telran.springcontainerconfigexample.Country">  
        <property name="name" value="France"/>  
        <property name="code" value="FR"/>  
        <property name="languale" value="French"/>  
    </bean>  
  
    <bean name="myValidator" class="de.telran.springcontainerconfigexample.Validator">  
        <property name="country" ref="france"/>  
    </bean>  
  
</beans>
<beans xmlns="http://www.springframework.org/schema/beans"  
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">  
  
    <bean name="france" class="de.telran.springcontainerconfigexample.Country">  
        <property name="name" value="France"/>  
        <property name="code" value="FR"/>  
        <property name="languale" value="French"/>  
    </bean>  
  
    <bean name="myValidator" class="de.telran.springcontainerconfigexample.Validator">  
        <property name="country" ref="france"/>  
    </bean>  
</beans>           

достаются бины из контекста  **спринг приложения** 
ApplicationContext context = new ClassPathXmlApplicationContext("applicfnionContext.xml");  
Country france = (Country) context.getBean("france");  
System.out.println(france);  
  
Validator validator = (Validator) context.getBean("myValidator");  
validator.validate();
в **спринг_контексте** классы создаются в **единственном** экземпляре 
такие объекты називаются **синглтонами** 

#### xml конфигурация создает
**инверсию** **зависимостей** 

## джава конфиг

додаем классу аннотацию @**Configuration**
додаем методам аннотацию @**Bean**

@Configuration  
public class AppContext {  
  
//    @Bean  
//    public Country france() {  
//        Country country = new Country();  
//        country.setName("France");  
//        country.setCode("FR");  
//        country.setLanguale("French");  
//  
//        return country;  
//    }  
//  
//    @Bean(name = "myValidator")  
//    public Validator validator() {  
//        Validator validator = new Validator();  
//        validator.setCountry(france());  
//        return validator;  
//    }
если имя метода не совпадает топишем его в аннотации **@Bean(name = "myValidator")**  с указанием правильного имени метода
например:
@Bean(name = "myValidator")  
public Validator validator() {  
    Validator validator = new Validator();  
    validator.setCountry(france());  
    return validator;

## автоконфигурация

для автоматического связывания классов их помечают специальной аннотацией @**ComponentScan** при этом конфигурационный файл остается таккой же или тот же как в случае с **джава конфиг**
@ComponentScan(**basePackages = "de.telran.springcontainerconfigexample.beans**")

в аннотации **@ComponentScan** указывается конкретное место расположения бинов (**basePackages = "de.telran.springcontainerconfigexample.beans**")
@PropertySource("classpath:application.properties") указывает путь к проперти которые находятся в aplication.properties

в автоконфигурации джава сама ищет бины то есть классы которые помечаются  @**Component**   но эти классы нужно потом инициировать 
можно создать пустой конструктор и в нем передать поля класса например:
public class Country {  
    private String name;  
    private String code;  
    private String languale;  
  
    public Country() {  
        this.setName("France");  
        this.setCode("FR");  
        this.setLanguale("French");  
    }
**связывание бинов**
чтобы связывать классы используют три способа:
- связывание полей
**@Autowired**  
**private Country country**;

- связывание через сеттер 
производится с указанием бина **@Autowired** сеттерам , кроме того нужен пустой конструктор , например:

@Autowired  
public void setValidator(Validator validator) {  
    this.validator = validator;  
}  
  
@Autowired  
public void setCountry(Country country) {  
    this.country = country;  
}

- связывание через конструктор
производится с указанием бина **@Autowired** конструктору, например:

@Autowired  
public UseBeans(Validator validator, Country country) {  
    this.validator = validator;  
    this.country = country;  
}


## настройки бинов

настройки бинов(конкретные их значения - **Захардкодженные**) хранят в отдельном файле п папке ресурсед ->  **application.properties)** 

в классе конструктор уже не нужен, а значение полей передаем так:
@Value("S{**country.language**}") где **country.language** имя поля зазначенное в пропертях (настройки бинов(конкретные их значения - **Захардкодженные**) хранят в отдельном файле п папке ресурсед ->  **application.properties)


