---
title: "DELIT методы"
category: "networking"
tags: ['repository', 'клиент', 'ответ', 'delit', 'проэкт']
status: "published"
created: "2026-03-24"
updated: "2026-03-24"
ai-processed: false
source: "manual"
quality: 1
related-files: []
---

﻿1   -----------
2   Связи: [[HTTP]] сервер  клиент [[запрос]] [[ответ]] [[проэкт на spring bot]]  
[[Репозиторий repository java]]  [[GET методы]]  [[POST методы]]  [[PUT методы]]  [[PATCH методы]] [[DELIT методы]] 
3   Теги: аннотаци  # 

## DELETE методы

для запуска приложения APP нужно сделать класс контроллера
он помечается аннотаци  @**PostMapping** , для передачи параметра используют два пути 
- @**PathVariable**  - информациябудет содержаться в URL 
- @**RequestParam** - Через реквест параметры как показано ниже:
@DeleteMapping("/all")
public void deleteByISBN(@RequestParam String isbn) {  
    library.removeIf(book -> book.getIsbn().equals(isbn));  
}

но если книги не сущепствует надо добавить :
@DeleteMapping("/all")  
public ResponseEntity<?> deleteByISBN(@RequestParam String isbn) {  
    library.removeIf(book -> book.getIsbn().equals(isbn));  
    return new ResponseEntity<>(HttpStatus.ACCEPTED);  
}
чтоб в постмане показало действительный статуc  **HttpStatus.ACCEPTED**, а не 200 OK

