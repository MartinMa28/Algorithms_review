import threading
import time


class Foo:
    def __init__(self):
        self._second_lock = threading.Lock()
        self._thrid_lock = threading.Lock()
        self._second_lock.acquire()
        self._thrid_lock.acquire()

    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        time.sleep(1)
        printFirst()
        #print('first')
        self._second_lock.release()

    
    def second(self, printSecond: 'Callable[[], None]') -> None:
        time.sleep(1)
        self._second_lock.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        #print('second')
        self._thrid_lock.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        time.sleep(1)
        self._thrid_lock.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        #print('third')
        self._thrid_lock.release()


def print_sth(sth: str):
    def inner_func():
        print(sth)

    return inner_func


if __name__ == "__main__":
    foo = Foo()
    x = threading.Thread(target=foo.first, args=(print_sth('first'),))
    y = threading.Thread(target=foo.second, args=(print_sth('second'),))
    z = threading.Thread(target=foo.third, args=(print_sth('third'),))
    
    x.start()
    y.start()
    z.start()

    x.join()
    y.join()
    z.join()
    print('finish')