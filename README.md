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

## 🐳 Быстрый старт (Docker)

Это самый простой способ запустить весь стек (App + Database) одной командой:

1. Склонируйте репозиторий:
   ```bash
   git clone [https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git](https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git)
   cd devops-engineer-from-scratch-project-313
   ```
2. Запустите проект:
   ```bash

    make up
   ```

Приложение будет доступно по адресу: http://localhost:8080

## 💻 Команды Makefile

| Команда | Описание |
|:---------|:----------|
| `make up` | Собрать образы и запустить проект в фоне |
| `make down` | Остановить контейнеры и удалить тома (очистка БД) |
| `make test` | Запустить pytest **внутри** Docker-контейнера |
| `make lint` | Проверить код линтером Ruff внутри контейнера |
| `make logs` | Посмотреть логи приложения в реальном времени |
| `make shell` | Зайти в терминал запущенного контейнера |

## 🧪 Тестирование

Все тесты изолированы. Перед каждым запуском база данных очищается автоматически через фикстуры, что гарантирует чистоту проверок пагинации и CRUD-операций.

## 🌍 Деплой

Приложение развернуто и доступно по адресу:
https://devops-engineer-from-scratch-project-313-llm2.onrender.com/

---

<br>

<p align="center">
  <a href="https://ru.hexlet.io/programs/devops-engineer" target="_blank">
    <img src="https://raw.githubusercontent.com/Hexlet/assets/master/images/hexlet_logo128.png" width="120px" alt="Hexlet Logo">
  </a>
  <br>
  Проект выполнен в учебных целях на платформе <a href="https://ru.hexlet.io/pages/about">Hexlet</a>
</p>