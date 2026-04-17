""" Mock Interview with Hitha: 16th April, 2026 """
""" Question:
Given a binary array nums (only 0s and 1s), 
return the length of the longest contiguous subarray with an equal number of 0s and 1s.

Input: nums = [0,1,0]
Output: 2
Explanation: [0,1] or [1,0]

max_len = 6
count_zero = 4
count_one = 3

nums = [0,1,0,0,1,1,0]
       -1 0 -1 -2 -1 0 -1
          l          r
Output: 6

nums = [0,1,0,0,1,0,0]
Output = 4

[-1, +1, -1, -1, +1, +1, -1]

prefix_map = {0: -1}
curr_sum = 0
max_len = 0
Index	Num	Transformed	curr_sum	Seen before?	Length	max_len
0	0	-1	-1	❌	—	0
1	1	+1	0	✅ (at -1)	1 - (-1) = 2	2

"""
from typing import List

class Solution:
    def longestSubarraywithEqualNumbers(self, nums: List[int]) -> int:
        add = 0
        pointer = 0
        max_len = 0
        prefix = {}
        for i,num in enumerate(nums):
            if num == 0:
                add -= 1
            else:
                add += 1
            prefix[add] = i
            if add == 0:
                max_len = max(i - pointer + 1, max_len)
                pointer = i
                
        return max_len
    
nums = [0,1,0,0,1,0,0]
obj = Solution()
print(obj.longestSubarraywithEqualNumbers(nums))