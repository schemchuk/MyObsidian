1   -----------
2   Связи: [[HTTP]] сервер  клиент [[запрос]] [[ответ]] [[проэкт на spring bot]]  
[[Репозиторий repository java]]  [[GET методы]]  [[POST методы]]  [[PUT методы]] [[PATCH методы]] [[DELIT методы]] 
3   Теги: аннотаци  # 

## PUT методы

обновляют всю информацию

для запуска приложения APP нужно сделать класс контроллера
он помечается аннотаци  @**PutMapping** 

если обекта нет, он **создастся**, а если есть то **перезапишется**

@PutMapping("/all")  
public ResponseEntity<Book> updateBook(@RequestBody Book book) {  
  
    if (library.contains(book)) {  
  
        int index = library.indexOf(book);  
        library.set(index, book);  
        return new ResponseEntity<>(book, HttpStatus.OK);  
    } else {  
        library.add(book);  
        return new ResponseEntity<>(book, HttpStatus.CREATED);  
    }