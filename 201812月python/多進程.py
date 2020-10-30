#coding=utf-8
from multiprocessing import Process
import os
import random
import time

def down(filename,num):
    print('启动下载进程，进程号[%d].' % os.getpid())
    print(f"開始下載{filename}...")
    sleeptime = random.randint(5,10)
    time.sleep(sleeptime)
    print(f"{filename}下載完成！耗費了{sleeptime}秒！")

def main():
    start = time.time()
    p1 = Process(target = down,args = ('Python从入门到住院',2))
    p1.start()
    p2 = Process(target = down,args =('Peking Hot.avi',2))
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print('总共耗费了%.2f秒.' % (end - start))

if __name__ == '__main__':
    main()
