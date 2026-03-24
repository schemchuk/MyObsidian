1   -----------
2   Связи: [[java  джава]]  [[синхронизация  Synchroniz]] коллекции 
3   Теги: #Date #LocalDate #LocalDateTime #ZonedDateTime #Instant #LokalTime

Существует два типы дат
- устаревшие  Date    01.01.1970, ms 
- теперь предпочитают Gregoriancalendar




LocalDate - класс из пакета java.time

Методы:

LocalDate now() - возвращает объект, который представляет текущую дату
LocalDate.of(int year, int month, int day) -возвращает объект, который представляет дату c определенным годом, месяцем и днем

getYear() - возвращает год
getMonthValue() - возвращает месяц
getDayOfMonth() - возвращает день месяца - 1 - 31
getDayOfYear() - возвращает день месяца - 1 - 365

plusDays(int n) - добавляет к дате количество дней
plusWeeks(int n) - добавляет к дате количество недель

minusDays(int n) - отнимает от даты некоторое количество дней


LocalDateTime - класс из пакета java.time

локальный объект даты и времени без информации о часовом поясе

LocalDataTime - неизменяемый объект даты и времени представляющий дату в формате
yyyy-MM-dd-HH-mm-ss.zzz

методы:

format() - используется для форматирования даты
get() - получить значение из указанного поля в виде int
now() - для получения текущей даты и времени

plusHours()
plusDays()
plusYears()







классы Date and Callendar изменяемые, что нехорошо

 class Instant это временная метка
 Для замера времени между инстантами используем класс Duration или использовать метод  System.currentTimeMilis, или System.nanoTime
В методах #LocalDate #LocalDateTime #ZonedDateTime #LokalTime  не используется конструктор,  время задается просто через точку после класса, т.е. вызываем метод напрямую.











