import requests
import html2text

s = requests.get('http://xakep.ru')
print(s.status_code)
# Создается экземпляр парсера
d = html2text.HTML2Text()
# Параметр, влияющий на то, как парсятся ссылки
d.ignore_links = True
# Текст без html-тегов
c = d.handle(s.text)
print(c)
