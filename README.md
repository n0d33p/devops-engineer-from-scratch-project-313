### Hexlet tests and linter status:
[![Actions Status](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions)
[![Project Checks](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/main.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/main.yml)

# Link Shortener (DevOps Project)

Современный сокращатель ссылок на базе **FastAPI** и **SQLModel**. Проект разработан в рамках курса DevOps-инженера на Hexlet и демонстрирует навыки проектирования архитектуры, контейнеризации и деплоя облачных приложений.

## 🚀 Возможности
- **Clean Architecture**: Реализован паттерн **Repository** для разделения бизнес-логики и работы с БД.
- **FastAPI API**: Быстрая и асинхронная обработка запросов.
- **PostgreSQL**: Надежное хранение данных.
- **Pagination**: Поддержка стандарта React Admin (`Content-Range` headers).
- **Sentry Integration**: Мониторинг ошибок и производительности.
- **Docker Ready**: Полная контейнеризация приложения (Python 3.14-alpine).

## 🛠 Требования
- **Docker** & **Docker Compose**
- **Make** (для удобного управления командами)
- **uv** (менеджер пакетов Python)

## 🛠 Запуск

### Основной способ (Docker Compose)
Рекомендуется для проверки работоспособности и деплоя. Все сервисы упакованы в единую сеть.

1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git](https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git)
   cd devops-engineer-from-scratch-project-313
   ```
2. Запустите проект через Docker Compose (автоматически поднимет БД, бэкенд и Nginx):
   ```bash
   make up
   ```
Приложение будет доступно на http://localhost:8080

## 💻 Команды Makefile

| Команда | Описание                                                   |
|:---------|:-----------------------------------------------------------|
| `make up` | Собрать и запустить все сервисы в Docker                   |
| `make down` | Остановить и удалить контейнеры                            |
| `make test` | Запустить тесты                                            |
| `make lint` | Проверить код линтером Ruff                                |
| `make run` | Запустить одновременно бэкенд и фронтенд локально          |


## 🧪 Тестирование

Тесты покрывают основные CRUD-операции и логику редиректов. Перед каждым запуском база данных очищается, что гарантирует независимость тестов.
## 🌍 Деплой

Приложение развернуто на Render с использованием Docker-контейнеров:
[Демо-версия проекта](https://devops-engineer-from-scratch-project-313-llm2.onrender.com/)

---

<br>

<a href="https://ru.hexlet.io/programs/devops-engineer" target="_blank">
  <img src="https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png" width="120px" alt="Hexlet Logo">
</a>

Проект выполнен в учебных целях на платформе [Hexlet](https://ru.hexlet.io/pages/about)