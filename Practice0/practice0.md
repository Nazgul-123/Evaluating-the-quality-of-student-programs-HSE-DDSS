# Практическая работа №0
## Цель
Положить начало разработке распределённой программной системы (DSS) для автоматизированной проверки программного кода студентов.

## Задачи
**1. Выбрать тему для Вашей новой DSS. &#x2611;**  
Тема: <<РАЗРАБОТКА ИС ДЛЯ ОЦЕНКИ ПРОГРАММНОГО КОДА СТУДЕНТОВ ПО ДИСЦИПЛИНЕ “ПРОГРАММИРОВАНИЕ”>>.  

---

**2. Создать репозиторий для работы над Вашей DSS. &#x2611;**    

---

**3. Выявить первоначальные требования к Вашей DSS. &#x2611;**  
**_Функциональные требования:_**
1. Получение отчета по заранее выделенным критериям.
2. Возможность изменения критериев преподавателем.
3. Получение уведомления после завершения проверки кода.
4. Возможность загрузки студенческих работ через интеграцию с GitHub и/или вручную;
5. Добавление резльутатов стат. анализатора в отчет по коду.   
* Возможность отслеживания прогресса студентов по версиям в рамках одной лабораторной и/или на протяжении всего курса;
(желательно)

**_Нефункциональные требования:_**
* Расширяемость (новые критерии проверки должны легко добавляться)
* Высокая производительность при обработке большого количества работ

 ---

**4. Создать модель предметной области Вашей DSS. &#x2611;**  

_**Use-Case диаграммы:**_
_Актеры:_
- Преподаватель
- Студент
- Администратор системы

_Варианты использования:_
- Преподаватель:
![Диаграмма вариантов использования для преподавателя drawio](https://github.com/user-attachments/assets/6936427d-c409-40a6-a328-f22037acba5f)

- Студент:
  - Загрузка кода на GitHub.
  - Получение обратной связи (возможно).   
![Диаграмма вариантов использования для студента drawio](https://github.com/user-attachments/assets/b23edfc0-1c0f-4a91-a0b3-93fc78e09929)

- Администратор:
  - Управление базой данных преподавателей.
  - Обновление ссылки на репозиторий работ студентов.   
![Диаграмма вариантов использования  для администратора](https://github.com/user-attachments/assets/c209cdf5-6034-4ba0-ac1d-590abfb6fbc0)

_**DDD:**_  
Event storming 
![design-event_storming_evaluate_student_code drawio](https://github.com/user-attachments/assets/2fae0a22-9169-4fc0-b4f1-ae4e9595e1f7)

Aggregate
![design-aggregate_ev_st_code drawio](https://github.com/user-attachments/assets/2c9f9384-9c4b-4334-937b-5cda734c0d58)
      
Глоссарий (Ubiquitous Language)
- Код: Исходный текст программы на языке C#, который они загружают на GitHub.
- Отчёт: Документ, содержащий оценку,комментарии по выделенным критериям.
- Метрики кода: Показатели, такие как тестовое покрытие, сложность, читаемость.
- Лабораторная работа: Задание, которое студент должен выполнить и сдать.

---

**5. Выбрать инструментарий (язык, IDE/редактор кода, etc.) для реализации Вашей DSS. &#x2611;**  
- Backend: Python, GitPython
- Frontend: Python, pyTelegramBotAPI 
- База данных: sqlLite3
- Машинное обучение: NLTK, Scikit–learn, PyTorch, Pandas, NumPy, Matplotlib

---

**6. Выбрать модель данных для реализации Вашей DSS: &#x2611;**  
   1. На уровне приложения - классы для сущностей
   2. На уровне хранения - реляционная модель

---

**7. Реализовать первоначальные требования (из п.3) к Вашей DSS. &#x2611;**  

---

**8. Загрузить первую версию DSS на веб-хостинг (Github, Gitlab, etc.) &#x2611;**  

---

## Требования
1. Выделите не менее 5 прецедентов для выбранной темы.
2. У модели предметной области обязательно должен быть глоссарий (определён Ubiquitous language).
3. Код должен быть покрыт автотестами (Unit, integration, e2e).
4. Необходимо настроить линтер и статический анализатор.
5. Необходимо подумать над версионированием и ведением истории изменений проекта.
6. В качестве экспертной области будет выступать преподаватель курса. Не забывайте обращаться к нему для выявления требований к системе.
