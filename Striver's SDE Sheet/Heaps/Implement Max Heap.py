class Solution:
    def initializeHeap(self):
        self.MaxHeap = []

    def insert(self, key):
        self.MaxHeap.append(-1 * key)
        self.MaxHeap.sort()

    def changeKey(self, index, new_val):
        self.MaxHeap[index] = -1 * new_val

    def extractMax(self):
        self.MaxHeap.pop(0)

    def isEmpty(self):
        if self.MaxHeap:
            return False
        return True

    def getMax(self):
        return self.MaxHeap[0] * -1

    def heapSize(self):
        return len(self.MaxHeap)


operation = [ "initializeHeap", "insert", "insert", "exctractMax", "getMax", "insert", "heapSize", "isEmpty", "exctractMax", "changeKey" , "getMax" ]

nums = [ [4], [1], [4], [0, 2] ]

obj = Solution()
obj.initializeHeap()
obj.insert(4)
obj.insert(1)
obj.extractMax()
print(obj.getMax())
obj.insert(4)
print(obj.heapSize())
print(obj.isEmpty())
obj.extractMax()
obj.changeKey(0, 2)
print(obj.getMax())