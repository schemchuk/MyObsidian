
1   -----------
2   Связи: Связи: [[HTTP]] сервер  клиент [[запрос]] [[ответ]] [[проэкт на spring bot]] [[java  джава]]  [[гит git hub]]
3   Теги:

#### создание репозитория 


[[Репозиторий repository java]] [[java  джава]]

Для каждой таблицы мы должны создать отображение в [[java  джава]] - 

для этого существует специальный тип файлов **entity ентити** сущность для работы с базами данных
**По джо классы** -классы для хранения данных

каждая колонка представляет собой **переменную класса**  *с определенным типом данных* который представляется таблицей
@Entity  
@Table(name = "Products")  
@AllArgsConstructor  
@NoArgsConstructor  
@Getter  
@Setter  
public class Products {  
    @Id // **ето уникальное поле Primary Cey** 
    @Column(name = "ProductId")  
    @GeneratedValue(strategy = GenerationType.IDENTITY)  
    private long productID;  
  
    @Column(name = "Name")  
    private String name;  
  
    @Column(name = "Description")  
    private String description;

если название колонки в таблице начинается с маленькой буквы, то [[аннотация]] @Column(name = "Name") **не пишется** 
в данном случае первые букви написания в джава коде и колонке не совпадают