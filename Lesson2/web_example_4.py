import requests
import shutil
import os

# Файл, который надо скачать
s = 'https://xakep.ru/robots.txt'

# С помощью функции os.path.split(s) вытаскиваем из строки путь к файлу и его имя
dirname, filename = os.path.split(s)

# GET-запрос в режиме stream=True для скачивания файла

r = requests.get(s, stream=True)

# Если ответ сервера удачен (200)
if r.status_code == 200:
    # Создаем файл и открываем его в бинарном режиме для записи
    with open(filename, 'wb') as f:
    # Декодируем поток данных на основе заголовка content-encoding
        r.raw.decode_content = True
        # Копируем поток данных из интернета в файл с помощью модуля shutil
        shutil.copyfileobj(r.raw, f)
