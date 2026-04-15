### Hexlet tests and linter status:
[![Actions Status](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/n0d33p/devops-engineer-from-scratch-project-313/actions)

# DevOps Project: Step 1 (Python Application)

Базовое Python-приложение на Flask, подготовленное в рамках первого шага обучения DevOps-инженера. Приложение представляет собой простой HTTP-сервер с проверочным маршрутом.

## Требования

Для запуска проекта вам понадобятся:
* **Python** 3.10 или выше
* **uv** (современный менеджер пакетов для Python)
* **make** (утилита для сборки и запуска)

## Установка

1. Склонируйте репозиторий:
```bash
   git clone https://github.com/n0d33p/devops-engineer-from-scratch-project-313.git
   cd devops-engineer-from-scratch-project-313 
   ```


Установите зависимости проекта с помощью uv:
```bash
uv sync
```

## Запуск приложения

Приложение запускается через Makefile. По умолчанию сервер поднимается на порту 8080.
```bash

make run
```
После запуска приложение будет доступно по адресу: http://localhost:8080

```bash
curl http://localhost:8080/ping 
```

