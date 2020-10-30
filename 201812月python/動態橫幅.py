import os
import time


def main():
    content = '熱烈慶祝中華人民共和國成立70週年！'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.5)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
