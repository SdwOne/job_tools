import pyperclip
import time
import re

old = ''
while True:
    s = pyperclip.paste()
    # Если содержимое буфера изменилось и содержит буквы латинского алфавита или цифры, мы дозаписываем его в файл monitoring.txt
    if s != old and re.search('\w', s):
        old = s
        with open('monitoring.txt', 'a', encoding='UTF-8') as f:
            f.write(f"{s}\n")

    # В конце витка делаем паузу в одну секунду, чтобы содержимое буфера обмена успело прогрузиться
    time.sleep(1)
