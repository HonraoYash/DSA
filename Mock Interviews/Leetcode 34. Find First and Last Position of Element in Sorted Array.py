""" Mock Interview; 19th March, 2026. with Hitha """

"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

# [5,7,7,8,8,10] 
         l  m  r

1. Find Left Boundary

Move left when nums[mid] >= target

Keep track of possible answer

2. Find Right Boundary

Move right when nums[mid] <= target

Keep track of possible answer
"""


from typing import List

class Solution:
      def findRange(self, nums: List[int], target: int) -> List[int]:
            opening = closing = -1

            # Finding the left boundary
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    opening = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            
            if opening != -1:
                left = opening
            else:
                return [-1,-1]

            # Finding the right boundary
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                   closing = mid
                   left = mid + 1
                elif nums[mid] < target:
                   left = mid + 1
                else:
                    right = mid - 1

            if closing != -1:
               return [opening, closing]
            else:
               return [-1, -1]

            # Time Complexity - O(logn + logn) = O(2logn) + O(logn)
            # Space Complexity - O(1)