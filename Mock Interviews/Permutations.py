""" Mock Interviews - 26th March, 2026. with Hitha """
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""
nums = [1,2,3]

class Solution:
      def permutations(self, nums):
        if len(nums) == 0:
           return [[]]
    
        res = []
        perms = self.permutations(nums[1:])
        for perm in perms:
            for j in range(len(perm)+1):
                p_copy = perm.copy()
                p_copy.insert(j, nums[0])
                res.append(p_copy)

        return res
        
nums = [1,2,3]
print(Solution().permutations(nums))