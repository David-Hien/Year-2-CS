from lib.queue import queue
from lib.stack import stack
import random

class order:
    def __init__(self, raw:queue):
        self.raw = raw

    def __repr__(self) -> str:
        return str(self.raw)

    def sort_q2s(self) -> stack:
        ordered = stack()
        while not self.raw.isEmpty():
            max = 0
            current = self.raw.dequeue()
            while not self.raw.isEmpty():
                if max < current:
                    max = current
                
                self.raw.enqueue(max)
                current = self.raw.dequeue()
            
            ordered.push(max)

        return ordered


def get_queue():
    q = queue()
    for i in range(10):
        q.enqueue(random.randint(1, 7))

    return q

test1  = order(get_queue())
print(test1)
test2  = order(get_queue())
test3  = order(get_queue())
test4  = order(get_queue())

print(test1.sort_q2s())