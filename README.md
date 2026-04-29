### Hexlet tests and linter status:
[![Actions Status](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions)
[![Project Checks](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/main.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/main.yml)

# Link Shortener (DevOps Project)

Современный сокращатель ссылок на базе **FastAPI** и **SQLModel**. Проект разработан в рамках курса DevOps-инженера на Hexlet и демонстрирует навыки контейнеризации, автоматизации и деплоя облачных приложений.

## 🚀 Возможности
- **FastAPI API**: Быстрая и асинхронная обработка запросов.
- **PostgreSQL**: Надежное хранение данных.
- **Pagination**: Поддержка стандарта React Admin (`Content-Range` headers).
- **Docker-ready**: Полная оркестрация через Docker Compose.
- **Sentry Integration**: Мониторинг ошибок в реальном времени.

## 🛠 Требования
- **Docker** & **Docker Compose**
- **Make** (для удобного управления командами)
- **uv** (если планируется запуск вне контейнеров)

## 🛠 Запуск

Для одновременной работы бэкенда и фронтенда с поддержкой Hot Reload:

1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git](https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git)
   cd devops-engineer-from-scratch-project-313

2. Поднимите базу данных (проект использует Docker для управления базой данных):
   ```bash
   make up
   ```
3. Запустите приложение
   ```bash
   make run
   ```
Бэкенд будет доступен на http://localhost:8080, фронтенд — на http://localhost:5173.

## 💻 Команды Makefile

| Команда | Описание |
|:---------|:----------|
| `make up` | Запустить только базу данных PostgreSQL в Docker |
| `make down` | Остановить базу данных |
| `make test` | Запустить тесты через uv run pytest |
| `make lint` | Проверить код линтером Ruff |
| `make run` | Запустить одновременно бэкенд и фронтенд локально |


## 🧪 Тестирование

Все тесты изолированы. Перед каждым запуском база данных очищается автоматически через фикстуры, что гарантирует чистоту проверок пагинации и CRUD-операций.

## 🌍 Деплой

Приложение развернуто и доступно по адресу:
https://devops-engineer-from-scratch-project-313-llm2.onrender.com/

---

<br>

<a href="https://ru.hexlet.io/programs/devops-engineer" target="_blank">
  <img src="https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png" width="120px" alt="Hexlet Logo">
</a>

Проект выполнен в учебных целях на платформе [Hexlet](https://ru.hexlet.io/pages/about)