# Отчет по лабораторной работе  
* Проект находится в отдельном репозитории: https://github.com/Nazgul-123/Code-evaluation-system

## Тема: Распределение DSS на микросервисы  

---

## Цель работы  
Разделить монолитную систему **DSS** на микросервисную архитектуру, используя **Docker Compose** и **RabbitMQ** для асинхронного взаимодействия.  

---

## Ход выполнения работы  

### 1. Определение API DSS  
Выбран **асинхронный (Event-based) API** с использованием **RabbitMQ**.  

**Обоснование:**  
- DSS требует выполнения долгих операций анализа кода, **RPC будет блокировать** выполнение других задач.  
- **Асинхронная архитектура** позволяет обрабатывать запросы параллельно, улучшая масштабируемость и отказоустойчивость.  
- **RabbitMQ** выступает брокером сообщений между сервисами.  

---

### 2. Разделение системы на микросервисы  
Выделены **четыре микросервиса** на основе логических контекстов:  

| **Микросервис**        | **Описание** |
|-----------------------|-------------|
| **Bot** | Телеграм-бот, принимающий запросы от пользователей и отправляющий отчеты. |
| **GitHub Service** | Получает код пользователя из GitHub и передает в очередь на анализ. |
| **Analysis Service** | Выполняет анализ кода (статический анализатор + LLM) и передает результат в отчетный сервис. |
| **Report Service** | Формирует итоговый отчет по анализу кода и отправляет в сервис чат-бота для отправки пользователю. |

Сервисы взаимодействуют через **RabbitMQ**, используя очереди сообщений.  

---

### 3. Взаимодействие сервисов  

**Процесс обработки запроса:**  
1. **Пользователь** нажимает кнопку в Телеграм-боте.  
2. **Bot Service** отправляет сообщение в очередь `github_queue`.  
3. **GitHub Service** загружает код студента и отправляет его в `analysis_queue`.  
4. **Analysis Service** анализирует код и передает результаты в `report_queue`.  
5. **Report Service** формирует итоговый отчет и отправляет его в `bot_queue`.  
6. **Bot Service** получает отчет и отправляет его пользователю в Телеграм.  

**Очереди в RabbitMQ:**  
- `github_queue` → получение кода  
- `analysis_queue` → анализ кода  
- `report_queue` → генерация отчета  
- `bot_queue` → отправка отчета пользователю  

---

### 4. Docker-инфраструктура  
Все сервисы развернуты с помощью **Docker Compose**:  

```yaml
version: '3.8'

services:
  rabbitmq:
    image: "rabbitmq:3-management"
    container_name: rabbitmq
    ports:
      - "5672:5672"
      - "15672:15672"  # Для веб-интерфейса
    networks:
      - app_network

  github_service:
    build:
      context: .
      dockerfile: domain/aggregate/github_service/Dockerfile
    env_file:
      - .env
    container_name: github_service
    restart: always
    networks:
      - app_network
    depends_on:
      - rabbitmq

  report_service:
    build:
      context: .
      dockerfile: domain/aggregate/report_service/Dockerfile
    container_name: report_service
    restart: always
    networks:
      - app_network
    depends_on:
      - rabbitmq

  analysis_service:
    build:
      context: .
      dockerfile: models/Dockerfile
    container_name: analysis_service
    restart: always
    networks:
      - app_network
    depends_on:
      - rabbitmq

  bot:
    build:
      context: .
      dockerfile: bot/Dockerfile
    env_file:
      - .env
    container_name: bot
    restart: always
    volumes:
      - ./bot/code_evaluation.db:/app/code_evaluation.db
    networks:
      - app_network
    depends_on:
      - rabbitmq
      - github_service
      - report_service
      - analysis_service

networks:
  app_network:
    driver: bridge
```

- Каждый сервис работает в отдельном контейнере.  
- Все сервисы связаны через сеть `app_network`.  
- RabbitMQ выступает посредником для обмена сообщениями.  

---

### 5. Покрытие кода автотестами
Тесты были доработаны.

---

### 6. Линтеры и статический анализ  
Включен линтер Pylint. 

---

## Выводы  
✔️ **Разделение системы на микросервисы выполнено.**  
✔️ **API DSS реализован как асинхронный (Event-based).**  
✔️ **Выделены 4 микросервиса, взаимодействующие через RabbitMQ.**  
✔️ **Docker Compose используется для развертывания системы.**  
✔️ **Код покрыт автотестами.**  
✔️ **Линтеры подключены.**  
✔️ **Один из микросервисов (Analysis Service) является потоковым обработчиком задач (consumer).**  

![image](https://github.com/user-attachments/assets/b7c549b2-6a70-4cf4-b99a-1e273e34b144)

