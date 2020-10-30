from threading import Lock,Thread
class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.Flock = Lock()
        self.Block = Lock()
        self.FBlock = Lock()
        self.nlock = Lock()

        self.Flock.acquire()
        self.Block.acquire()
        self.FBlock.acquire()


    # printFizz() outputs "fizz"
    def fizz(self):
        for i in range(3,self.n+1,3):
            self.Flock.acquire()
            print("Fizz")
            self.nlock.release()
    # printBuzz() outputs "buzz"
    def buzz(self):   
        for i in range(5,self.n+1,5):
            self.Block.acquire()
            print("buzz")
            self.nlock.release()
    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self):  
        for i in range(15,self.n+1,15):
            self.FBlock.acquire()
            print("fizzbuzz")
            self.nlock.release()
    # printNumber(x) outputs "x", where x is an integer.
    def number(self):  
        for i in range(1,self.n+1):
            self.nlock.acquire()
            if i%15 ==0:
                self.FBlock.release()
            elif i%5 ==0:
                self.Block.release()
            elif i%3 ==0:
                self.Flock.release()
            else:
                print(i)
                self.nlock.release()

ins = FizzBuzz(15)
t1 = Thread(target=ins.fizz)
t1.start()
t2 = Thread(target=ins.buzz) 
t2.start()
t3 = Thread(target=ins.fizzbuzz)
t3.start()
t4 = Thread(target=ins.number)
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print("OK!")
#好像遇到了一個問題，1-14都可以正常輸出最後的“OK”,超過15就會 有2個綫程卡住 不會輸出最後的“OK”
#這好像就是爲什麽提交一直超時的原因 
#但是 for what? 求解 感激！

