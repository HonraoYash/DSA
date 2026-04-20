""" Mock Interview with Ellika: 20th April, 2026 """
"""
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no 
such integer.
void add(int value) insert value to the queue.


Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1

"""


class FirstUnique:
    def __init__(self, nums):    
        self.queue = nums      
        self.frequency = { }               
        for num in self.queue:
            self.frequency[num] = 1 + self.freqeuncy.get(num, 0)
        
    def showFirstUnique(self):     
        if not self.queue:
            return -1
        
        for i in range(len(self.queue)):
            if self.frequency[self.queue[i]] == 1:
                return self.queue[i]
            
        return -1
    
    def add(self, value):       
        self.queue.append(value)
        self.frequency[value] = 1 + self.freqeuncy.get(value, 0)
        
    # Space Complexity - O(N)
        
        
        
        