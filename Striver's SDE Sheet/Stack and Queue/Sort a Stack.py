""" We pop the top element of the stack, sorted the rest of the stack, and then insert that top element in the correct position.
    We do this recursively until the stack is sorted.
    Base case is when the stack is empty, we just return the stack.
    Base case is when the top element of the stack is greater than the element to be inserted, we just insert the element at the top of the stack.
    Base case for inserting is, if the stack is empty or the top element of the stack is less than the element to be inserted, 
    we just insert the element at the top of the stack.
    Time Complexity: O(n^2) - N recursive calls, each insert takes O(N)
    Space Complexity: O(n)
    where n is the number of elements in the stack.
"""
class Solution:
    def insert(self, stack, x):
        if not stack or stack[-1] <= x:
            stack.append(x)
            return
        temp = stack.pop()
        self.insert(stack, x)
        stack.append(temp)

    def sortStack(self, stack):
        if not stack:
            return stack
        x = stack.pop()
        self.sortStack(stack)
        self.insert(stack, x)
        return stack