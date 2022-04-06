import requests

user = 'kitty2007'
message = '(* ^ w ^)'

# Открываем файл в бинарном режиме
with open('payload.php', 'rb') as f:
    # POST-запрос с отправкой файла
    r = requests.post("http://site.ru/upload.php", files={'misc.php': f}, data={'user': user, 'message': message})
print(r.status_code)