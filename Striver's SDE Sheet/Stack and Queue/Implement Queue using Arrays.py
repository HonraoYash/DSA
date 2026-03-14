class ArrayQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop(0) if self.queue else None

    def peek(self):
        return self.queue[0]   if self.queue else None   

    def isEmpty(self):
        return not self.queue

    def size(self):
        return len(self.queue)

    def printQueue(self):
        return self.queue

    def clearQueue(self):
        self.queue = []