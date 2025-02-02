Структура проекта
```
/project-root
│── main.py                     # Точка входа
│── requirements.txt             # Зависимости Python
│── config/                      # Конфигурационные файлы
│── internal/
│   │── domain/                  
│   │   │── user.py               # Сущности пользователей (админ, преподаватель, студент)
│   │   │── code.py                 # Сущности по работам студентов
│   │── usecase/                 
│   │   │── github_service.py    # Работа с GitHub
│   │   │── code_service.py   # БЛ обработки кода
│   │   │── report_service.py  # Генерация отчетов
│   │── repository/              
│   │   │── database.py       # Работа с SQLite
│   │   │── telegram_bot.py      # Телеграм-бот
│── models/                      # ML-модели для анализа кода
│── tests/                       # Тесты
│── scripts/                     # Вспомогательные скрипты
│── docs/                        # Документация
```

---

## **Как запустить систему?**
1. **Установите зависимости из requirements.txt**
```commandline
pip install -r requirements.txt
```
2. **Запустите систему**
```commandline
python main.py
```
3. **Бот начнет работать**, принимая команды `/start`, `/upload` и `/report`.
   

---

## **Как запускать тесты?**  
1. Установите `pytest` и `pytest-mock`:  
   
```bash
pip install pytest pytest-mock
```

2. Запустите тесты:  
   
```bash
pytest tests/
```
