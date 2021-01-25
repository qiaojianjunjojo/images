from threading import Condition,Thread


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self._cv = Condition()
        self._p = 0

    def zero(self):
        for i in range(self.n):
            with self._cv:
                self._cv.wait_for(lambda: self._p == 0)
                print(0,end = '')
                self._p = 1 if i%2 == 0 else -1
                self._cv.notify_all()
        
    def even(self):
        for i in range(2, self.n+1, 2):
            with self._cv:
                self._cv.wait_for(lambda: self._p == -1)
                print(i,end= '')
                self._p = 0
                self._cv.notify_all()
        
    def odd(self):
        for i in range(1, self.n+1, 2):
            with self._cv:
                self._cv.wait_for(lambda: self._p == 1)
                print(i,end = '')
                self._p = 0
                self._cv.notify_all()

a = ZeroEvenOdd(10)
t1 = Thread(target=a.zero)
t1.start()
t2 = Thread(target=a.odd)
t2.start()
t3 = Thread(target=a.even)
t3.start()

