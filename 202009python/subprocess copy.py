# import threading
# from time import time,sleep

# def add(counter,i):
#     sleep(1)
#     counter[0]+=1
#     print(f'{counter[0]},綫程號{i}')


# def main():
#     counter = [0]
#     for i in range(1,11):
        
#         t = threading.Thread(target=add,args=(counter,i))
        
#         t.start()

# if __name__ == "__main__":
#     main()

# import threading
# import time
# from threading import RLock,Condition

# class MyThread(threading.Thread):
#     def __init__(self,lock,name):
#         threading.Thread.__init__(self)
#         self.lock = lock
#         self.name = name

#     def run(self):
#         time.sleep(1)
#         self.lock.acquire()
#         print(self.name)
#         self.lock.release()

# if __name__ == '__main__':
#     lock = threading.Lock()
#     for i in range(1,10):
#         t = MyThread(lock,i)
#         t.start()



import threading
from time import sleep

class Seeker(threading.Thread):
    def __init__(self,cond,name):
        threading.Thread.__init__(self)
        self.cond = cond
        self.name = name

    def run(self):
        sleep(1)
        self.cond.acquire()
        print("我把眼睛蒙上了")
        self.cond.notify()
        self.cond.wait()

        print("我找到你了")

        self.cond.notify()
        print("我赢了")
        self.cond.release()  #10.释放锁
        


class Hinder(threading.Thread):
    def __init__(self,cond,name):
        threading.Thread.__init__(self)
        self.cond = cond
        self.name = name

    def run(self):
        self.cond.acquire()
        self.cond.wait()
        print("我已经藏好了")
        self.cond.notify()
        self.cond.wait()

        print("被你找到了")

        self.cond.release()


cond = threading.Condition()
seek = Seeker(cond,"seek")
hind = Hinder(cond,"hind")
seek.start()
hind.start()