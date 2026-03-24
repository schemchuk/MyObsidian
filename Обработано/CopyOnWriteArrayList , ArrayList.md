ArrauList в многопоточности CopyOnWriteArrayList

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |
|     |     |     |     |



1   -----------
2   Связи:  [[java  джава]]  [[синхронизация  Synchroniz]]  [[парралельные коллекции]]
 List  LinkeldList  Set  TreeSet   Map  TreeMap   HashMap  [[HashSet , хеш таблицы, HashMap]]   [[CopyOnWriteArrayList , ArrayList]]  коллекции  [[многопоточность]]  [[парралельные коллекции]]
3   Теги: [[CopyOnWriteArrayList , ArrayList]]

При попытке изменения информации в CopyOnWriteArrayList создается копия ArrauList 
каждый [[поток]] работает с копией и имеет механизм внутренней синхронизации данных после его завершения
используетсядля чтения несколькими потоками и **вожможностью** *иногда* что-то записывать.