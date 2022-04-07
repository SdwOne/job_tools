import shutil
import requests

# Получаем список хостов
with open('hosts.txt', 'r') as h:
    hosts = h.read().splitlines()

for host in hosts:
    # TODO Сделать функцию, которая будет принимать на вход в качестве аргументов список хостов и список искомых файлов
    # TODO Сохранять найденные файлы в каталогах, соответствующих списку хостов
    robots = f'{host}robots.txt'
    sitemap = f'{host}sitemap.xml'

    r = requests.get(robots, stream=True)
    if r.status_code == 200:
        with open('robots.txt', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print(f'Файл robots.txt на сайте {host} не найден.')

    r = requests.get(sitemap, stream=True)
    if r.status_code == 200:
        with open('sitemap.xml', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        print(f'Файл sitemap.xml на сайте {host} не найден.')