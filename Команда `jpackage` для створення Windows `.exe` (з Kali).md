1   -----------
2   Связи: [[Команда x00T0x00 для створення Windows x00T1x00 (з Kali)]]
3   Теги

## Виконай з кореня проєкту (~/IdeaProjects/PostExAgent/):jpackage \
  --type app-image \
  --input target \
  --name PostExAgent \
  --main-jar PostExAgent-1.0-SNAPSHOT.jar \
  --main-class com.agent.postexagent.Main \
  --runtime-image ~/tools/win-jre/jdk-17.0.11+9-jre \
  --dest dist/windows
  
  🧪 Результат
буде створено: dist/windows/PostExAgent/PostExAgent.exe

він запуститься на Windows без JDK/JRE

у вікні cmd.exe або в фоновому режимі (пізніше можемо прибрати консоль)