import threading
from time import sleep

#商品
product = 500
#条件变量
con = threading.Condition(threading.Lock())

#生产者类
#继承Thread类
class Producer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        global product
        while True:
            #如果获得了锁
            if con.acquire():
                #处理产品大于等于500和小于500的情况
                if product > 100:
                    #如果大于等于500，Producer不需要额外操作，于是挂起
                    con.wait()
                else:
                    product += 50
                    message = self.name + " produced 50 products. " + str(product)
                    print(message)
                    #处理完成，发出通知告诉Consumer
                    con.notify()
                #释放锁
                con.release()
                sleep(1)
#消费者类
#继承Thread类
class Consumer(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        global product
        while True:
            #如果获得了锁
            if con.acquire():
                #处理product小于等于100和大于100的两种情况
                if product <= 100:
                    #如果小于等于100，Consumer不需要额外操作，于是挂起
                    con.wait()
                else:
                    product -= 10
                    message = self.name + " consumed 10 products. " + str(product)
                    print(message)
                    #处理完成，发出通知告诉Producer
                    con.notify()
                #释放锁
                con.release()
                sleep(1)
                
def main():
    #创建两个Producer
    for i in range(2):
        p = Producer('Producer-%d'%i)
        p.start()
    #创建三个Consumer
    for i in range(3):
        c = Consumer('Consumer-%d'%i)
        c.start()

if __name__ == '__main__':
    main()