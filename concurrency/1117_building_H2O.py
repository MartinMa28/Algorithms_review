from threading import Semaphore, Lock

class H2O:
    def __init__(self):
        self.hy_sema = Semaphore(value=2)
        self.oxy_sema = Semaphore(value=0)
        self.oxy_mutex = Lock()


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hy_sema.acquire()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.oxy_sema.release()
        
        
    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.oxy_mutex:
            self.oxy_sema.acquire()
            self.oxy_sema.acquire()
            
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.hy_sema.release()
        self.hy_sema.release()