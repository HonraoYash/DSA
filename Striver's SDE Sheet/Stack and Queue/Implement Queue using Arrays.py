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

""" The above is my implementation of the queue using arrays.
    But since we are asked to implement queue using arrays, we should use a fixed size array.
    And we should use a front and rear pointer to implement the queue.
"""

class ImplementQueueUsingArrays:
    def __init__(self):
        self.queue = [None] * 4
        self.start = -1
        self.end = -1
        self.size = 4
        self.currentSize = 0

    def push(self, x):                        # Time Complexity: O(1)
        if self.currentSize == 4:
            return "Queue is full"
        if self.start == -1:
            self.start += 1
            self.end += 1
        else:
            self.end = (self.end + 1) % self.size
        self.queue[self.end] = x
        self.currentSize += 1

    def pop(self):                            # Time Complexity: O(1)
        if self.start == -1:
            return None
        element = self.queue[self.start]
        if self.currentSize == 1:
            self.start =  self.end = - 1
        else:
            self.start = (self.start + 1) % self.size
        self.currentSize -= 1
        return element

    def top(self):                            # Time Complexity: O(1)
        if self.currentSize == 0:
            return None
        return self.queue[self.start]

    def size(self):                            # Time Complexity: O(1)
        return self.currentSize

    def isEmpty(self):                        # Time Complexity: O(1)
        return self.currentSize == 0

    def printQueue(self):                     # Time Complexity: O(1)
        return self.queue[:self.currentSize]

    def clearQueue(self):                     # Time Complexity: O(1)
        self.queue = [None] * 4
        self.start = -1
        self.end = -1
        self.currentSize = 0
    # Space Complexity: O(size)

obj = ImplementQueueUsingArrays()
print(obj.isEmpty())
obj.push(1)
print(obj.pop())
print(obj.isEmpty())
print(obj.printQueue())
obj.clearQueue()
print(obj.printQueue()) # Output: []        

""" We have implemented the queue using arrays, the only disadvantage is that we need to know the size of the array upfront. It's not dynamic in nature. 
    If we want to implement a dynamic queue, we have to use a linked list.
"""