from curses import noecho


class Node:
    def __init__(self, val: int, next: Node) -> None:
        self.val = val
        self.next = next

class ImplementStackUsingLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):                        # Time Complexity: O(1)
        node = Node(x, self.top)
        self.top = node
        self.size += 1
    
    def pop(self):                            # Time Complexity: O(1)
        temp = self.top.next
        element = self.top.val
        self.top.next = None
        self.top = temp
        self.size -= 1
        return element

    def top(self):                            # Time Complexity: O(1)
        return self.top.val

    def isEmpty(self):                        # Time Complexity: O(1)
        return self.top is None

    def size(self):                            # Time Complexity: O(1)
        return self.size

    def printStack(self):                        # Time Complexity: O(1)
        temp = self.top
        while temp:
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def clearStack(self):                        # Time Complexity: O(1)   
        self.top = None
        self.size = 0

    # Space Complexity: O(N) (dynamic)
    
obj = ImplementStackUsingLinkedList()
obj.push(1)
obj.push(2)
obj.push(3)
obj.printStack()
print(obj.pop())
obj.printStack()