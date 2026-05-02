""" Mock Interview with Mahima: 1st May, 2026 """
'''

Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        print(answer)
        prod = 1
        for i, num in enumerate(nums):
            answer[i] = prod
            prod *= num
        
        print(answer)
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= prod
            prod *= nums[i]
        print(answer)
            
        return answer
        # Time Complexity - O(N)
        # Space Complexity - O(1) + O(N)(answer array)
    
nums = [1,2,3,4]
obj = Solution()
print(obj.productExceptSelf(nums))