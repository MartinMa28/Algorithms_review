import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self._bar_lock = threading.Lock()
        self._foo_lock = threading.Lock()
        self._bar_lock.acquire()
        

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self._foo_lock.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self._bar_lock.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self._bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self._foo_lock.release()