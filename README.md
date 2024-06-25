# Plinor_test_task
Test Task For Plinor

## Описание

High Load API - это высоконагруженное REST API, созданное с использованием FastAPI. Оно способно обрабатывать большое количество входящих данных, агрегировать их и предоставлять визуализацию в виде таблиц и графиков.

- **app/**: Директория для основного приложения.
  - **__init__.py**: Файл для инициализации модуля.
  - **main.py**: Главный файл приложения, содержит запуск FastAPI сервера.
  - **models.py**: Файл для описания моделей данных (Pydantic).
  - **database.py**: Файл для работы с базой данных.
  - **views.py**: Файл для описания маршрутов и логики обработки запросов.
  - **utils.py**: Файл для вспомогательных функций.
  - **test_load.py**: Файл для нагрузочного тестирования API.
- **requirements.txt**: Файл для указания зависимостей проекта.
- **README.md**: Файл с описанием проекта и инструкциями по установке и использованию.

## Установка и запуск

```bash
git clone https://github.com/alexandrLes/Plinor_test_task.git
cd Plinor_test_task
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
(Адрес - http://127.0.0.1:8000)
curl -X POST "http://127.0.0.1:8000/events/" -H "Content-Type: application/json" -d '{"ts": 1111111, "a": 1, "B": 7, "C": 3}'
curl "http://127.0.0.1:8000/aggregate/?timeframe=hour"

Нагрузочное тестирование:
python test_load.py

