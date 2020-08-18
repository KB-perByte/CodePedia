from threading import Lock
import threading
class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo) -> None:
        for i in range(self.n):
            self.foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar) -> None:
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()


fb = FooBar(6)

def pr():
    print('yey')
    return 

def br():
    print('nen')
    return

fb.foo(pr)
for i in threading.enumerate():
    print(i)
fb.bar(br)
