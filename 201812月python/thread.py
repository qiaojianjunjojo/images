#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time

print(threading.active_count())
print(threading.enumerate())
print(threading.current_thread())

def thread_job():
    print('This is a thread of %s' % threading.current_thread())
    print(time.time())

def new_job():
    print('another new thread',end ='/')
    print(time.time(),end='/')
          
def main():
    thread = threading.Thread(target=thread_job,)   # 定义线程 
    thread.start()  # 让线程开始工作
    thread2 = threading.Thread(target=new_job)
    thread2.start()
    
if __name__ == '__main__':
    main()
