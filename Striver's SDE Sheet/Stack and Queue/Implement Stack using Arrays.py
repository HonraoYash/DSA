class ArrayStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def top(self):
        return self.stack[-1] if self.stack else None

    def isEmpty(self):
        return not self.stack

    def size(self):
        return len(self.stack)

    def printStack(self):
        return self.stack

    def clearStack(self):
        self.stack = []

""" The above is my implementation of the stack using arrays.
    But according to Striver, we shouldn't use the .pop() methods and all, and it should be purely using arrays and pointers.
    But, we need to use a fixed sizr array in this case, which we can ask the interviewer what size of array can I consider.
"""
class ImplementStackUsingArrays:
    def __init__(self):
        self.stack = [None] * 10
        self.top = -1

    def push(self, x):                    # Time Complexity: O(1)
        if self.top >= len(self.stack) - 1:
            return "Stack is full"
        self.top += 1
        self.stack[self.top] = x

    def pop(self):                        # Time Complexity: O(1)
        if self.top == -1:
            return None
        res = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return res

    def top(self):                        # Time Complexity: O(1)
        if self.top == -1:
            return None
        return self.stack[self.top]

    def isEmpty(self):                    # Time Complexity: O(1)
        if self.top == -1:
            return True
        return False

    def size(self):                        # Time Complexity: O(1)
        return self.top + 1

    def printStack(self):                    # Time Complexity: O(1)
        return self.stack[:self.top + 1]

    def clearStack(self):
        self.stack = [None] * 10

    # Space Complexity: O(N)

obj = ImplementStackUsingArrays()
print(obj.isEmpty())
obj.push(1)
print(obj.pop())
print(obj.isEmpty())
print(obj.printStack())
obj.clearStack()
print(obj.printStack())

""" We have implemented the stack using arrays, the only disadvantage is that we need to know the size of the array upfront. It's not dynamic in nature. 
    If we want to implement a dynamic stack, we have to use a linked list.
"""