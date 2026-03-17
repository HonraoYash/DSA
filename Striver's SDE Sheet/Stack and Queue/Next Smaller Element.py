def nextSmallerElements(arr):
        nse = []
        stack = []

        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] < stack[-1]:
                stack.pop()
            if not stack:
                nse.append(-1)
            else:
                nse.append(stack[-1])
            stack.append(arr[i])
        return nse[::-1]

arr = [1, 2, 3, 4, 5]
print(nextSmallerElements(arr))