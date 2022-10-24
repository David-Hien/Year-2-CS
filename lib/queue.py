# Implementation
class queue:
    def __init__(self):  # constructor
        self.items = []

    def __repr__(self) -> str:  # string representation
        return str(self.items)

    def enqueue(self, item):  # add an item to the end
        self.items.insert(0, item)

    def dequeue(self):  # remove and return the first item
        return self.items.pop()

    def isEmpty(self):  # check if the queue is empty
        return self.items == []
