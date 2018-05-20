from multiprocessing import Process, Semaphore, Lock, Queue
import time

buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()

class a():
    def __init__(self, buffer, empty, full, lock):
        self.buffer = buffer
        self.empty = empty
        self.full = full
        self.lock = lock
        super().__init__()

class Consumer(a, Process):

    def run(self):
        while True:
            self.full.acquire()
            self.lock.acquire()
            self.buffer.get()
            print('Consumer pop an element')
            time.sleep(2)
            self.lock.release()
            self.empty.release()


class Producer(a, Process):

    def run(self):
        while True:
            self.empty.acquire()
            self.lock.acquire()
            self.buffer.put(1)
            print('Producer append an element')
            time.sleep(1)
            self.lock.release()
            self.full.release()


if __name__ == '__main__':
    p = Producer(buffer, empty, full, lock)
    c = Consumer(buffer, empty, full, lock)
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Ended!')