import os
import time
text = '熱烈慶祝中華人民共和國成立70週年！'
while True:   
    os.system('cls')
    print(text)
    time.sleep(0.2)
    text = text[1:] + text[0]
