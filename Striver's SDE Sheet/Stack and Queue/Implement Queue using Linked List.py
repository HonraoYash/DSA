class Node:
    def __init__(self, val: int, next: Node) -> None:
        self.val = val
        self.next = next

class ImplementQueueUsingLinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def push(self, x):                        # Time Complexity: O(1)
        node = Node(x, None)
        if self.start == None:
            self.start = self.end = node
        else:
            self.end.next = node
            self.end = node
        self.size += 1

    def pop(self):                            # Time Complexity: O(1)
        if self.start == None:
            return None
        element = self.start.val
        if self.start == self.end:
            self.start = None
            self.end = Node
        else:
            self.start = self.start.next
        self.size -= 1
        return element

    def top(self):                            # Time Complexity: O(1)
        return self.start.val

    def size(self):                            # Time Complexity: O(1)
        return self.size

    def isEmpty(self):                        # Time Complexity: O(1)
        return self.size == 0

    def printQueue(self):                        # Time Complexity: O(1)
        temp = self.start
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()         

    def clearQueue(self):                        # Time Complexity: O(1)
        self.start = None
        self.end = None
        self.size = 0

    # Space Complexity: O(N) (dynamic)

obj = ImplementQueueUsingLinkedList()
obj.push(1)
obj.push(2)
obj.push(3)
obj.printQueue()
print(obj.pop())
print(obj.printQueue())
print(obj.top())
print(obj.pop())
print(obj.printQueue())
print(obj.isEmpty())
# obj.size()
obj.clearQueue()
print(obj.printQueue())
# obj.size()
print(obj.isEmpty())