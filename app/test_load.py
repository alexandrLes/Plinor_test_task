import requests
import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

API_URL = "http://127.0.0.1:8000/events/"

# Количество источников данных
NUM_SOURCES = 100
# Количество событий на источник в секунду
EVENTS_PER_SECOND = 10

# Генерация случайного события
def generate_event(source_id):
    return {
        "ts": int(time.time()),
        "a": source_id % 9 + 1,
        "b": (source_id + 1) % 9 + 1,
        "c": (source_id + 2) % 9 + 1,
        "d": (source_id + 3) % 9 + 1,
        "e": (source_id + 4) % 9 + 1,
        "f": (source_id + 5) % 9 + 1
    }

# Отправка события на сервер
def send_event(event):
    headers = {"Content-Type": "application/json"}
    response = requests.post(API_URL, headers=headers, data=json.dumps(event))
    return response.status_code

# Имитирование источника данных
def simulate_source(source_id):
    for _ in range(EVENTS_PER_SECOND):
        event = generate_event(source_id)
        status_code = send_event(event)
        if status_code != 200:
            print(f"Failed to send event from source {source_id}, status code: {status_code}")

# Основная функция для многопоточного тестирования
def main():
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=NUM_SOURCES) as executor:
        futures = [executor.submit(simulate_source, i) for i in range(NUM_SOURCES)]
        for future in as_completed(futures):
            future.result()
    end_time = time.time()
    print(f"Test completed in {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
