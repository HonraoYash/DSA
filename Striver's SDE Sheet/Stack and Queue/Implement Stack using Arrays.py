class ArrayStack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def isEmpty(self):
        return not self.stack

    def size(self):
        return len(self.stack)

    def printStack(self):
        return self.stack

    def clearStack(self):
        self.stack = []


obj = ArrayStack()
print(obj.isEmpty())
obj.push(1)
print(obj.pop())
print(obj.isEmpty())