
1   -----------
2   Связи: [[HTTP]] сервер  клиент [[запрос]] [[ответ]] [[проэкт на spring bot]]  
[[Репозиторий repository java]]  [[GET методы]]  [[POST методы]]  [[PUT методы]] [[DELIT методы]] 
3   Теги: аннотаци  # 

## POSTметоды

для запуска приложения APP нужно сделать класс контроллера
он помечается аннотаци  @**PostMapping** , для передачи **тела  запроса** - - -----аргументов(книга ) по сети надо использовать @**RequestBody**   ,   например 
 @PostMapping("/all") void addBook(@RequestBody Book book) {  
    library.add(book);  
} метод ничего не возвращает потому **void**

Здесь я задаю чтобы **возвращало** добавленную книгу и **показывало** дополнительные параметры ответа, которые будут приходить от сервера  *HttpStatus.CREATED*: 

@PostMapping("/all")  
public ResponseEntity<Book> addBook(@RequestBody Book book) {  
    library.add(book);  
   return new ResponseEntity<>(book, HttpStatus.CREATED);  
}

POST [[запрос]] можно передать из командной строки а можно пользоваться программами **Postmann**