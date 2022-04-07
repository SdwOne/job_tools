# Читаем файл в список из строк
with open('victims.txt', 'r') as f:
    victims = f.read().splitlines()

domains = []
emails = []

for victim in victims:
    # Делим строки с данными жертв и берем только email
    email = victim.split('|')[1]
    emails.append(email)

for email in emails:
    # Выделяем из email-а домен
    domain = email.split('@')[1]
    if domain not in domains:
        domains.append(domain)
        # Для каждого нового домена создаем уникальный файл и добавляем в него соответствующий почтовый ящик
        with open(f'{domain}', 'w') as f:
            f.write(f'{email}\n')
    else:
        with open(f'{domain}', 'a') as f:
            f.write(f'{email}\n')