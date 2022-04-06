import socket

ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000]

print ("Ожидай, идет сканирование портов!")

# Получаем список хостов
with open('hosts.txt', 'r') as h:
    hosts = h.read().splitlines()

# Создаем пустой файл для записи результата
with open('result.txt', 'w', encoding='UTF-8') as r:
    r.write('')

for host in hosts:
    # В цикле перебираем порты из списка
    for port in ports:
        # Создаем сокет
        s = socket.socket()
        # Ставим тайм-аут в одну секунду
        s.settimeout(1)
        # Ловим ошибки
        try:
            # Пробуем соединиться, хост и порт передаем как список
            s.connect((host, port))
        # Если соединение вызвало ошибку
        except socket.error:
        # тогда ничего не делаем
            pass
        else:
            # Пишем результат в файл
            with open('result.txt', 'a') as r:
                r.write(f"{host}: {port} порт активен\n")
        # Закрываем соединение
            s.close

print("Сканирование завершено!")