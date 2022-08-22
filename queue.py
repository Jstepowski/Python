from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueu(self, item):
        self.buffer.appendleft(item)
    
    def dequeue(self):
        self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return (len(self.buffer))

