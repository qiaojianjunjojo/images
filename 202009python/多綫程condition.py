from threading import Condition,Thread
#wait_for(self, predicate, timeout=None) 比wait()方法多了一个predicate参数，predicate的返回值要求是bool值，
#返回为true时该线程就被唤醒，否则跟wait()一样
class FooBar:
    def __init__(self, n):
        self.n = n
        self._cv = Condition()
        self._p = True

    def foo(self):
        for i in range(self.n):
            with self._cv:
                self._cv.wait_for(lambda: not self._p)
                print("Foo")
                self._p = not self._p
                self._cv.notify()

    def bar(self):
        for i in range(self.n):
            with self._cv:
                self._cv.wait_for(lambda: self._p)
                print("Bar")
                self._p = not self._p
                self._cv.notify()

c = FooBar(10)
p1 = Thread(target=c.foo)
p2 = Thread(target=c.bar)
p1.start()
p2.start()