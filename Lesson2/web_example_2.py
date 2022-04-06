import requests
# Переменные, которые нужно отправить POST-запросом
user = 'coolhacker'
message = 'You have been pwned!!!'
# Делаем POST-запрос и передаем словарь из полей
r = requests.post("http://site.ru/guest.php", data={'user': user, 'message': message})
print(r.status_code)