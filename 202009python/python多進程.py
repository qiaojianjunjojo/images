from multiprocessing import Process
import subprocess
from time import time, sleep
from random import randint


def down(filename):
    print("開始下載"+filename)
    num =randint(5, 10)
    sleep(num)
    print(filename + "下載結束！")


def main():
    '''
    通过Process类创建了进程对象，通过target参数我们传入一个函数来表示进程启动后要执行的代码，后面的args是一个元组，
    它代表了传递给函数的参数。Process对象的start方法用来启动进程，而join方法表示等待进程执行结束。
    '''
    starttime = time()
    p1 = Process(target=down,args=("python從入門到入土",))
    p1.start()
    p2 = Process(target=down,args=("c#教程",))
    p2.start()
    p1.join()
    p2.join()
    endtime = time()
    print(endtime-starttime)


if __name__ == "__main__":
    main()


