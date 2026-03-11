class Solution:
    def maxSubArray(self, nums):
        """ Brute Force - Try out all the possible subarrays
            Use 3 nested loops to iterate through the array
            Time Complexity: O(n^3)
            Space Complexity: O(1)
            where n is the number of elements in the array
            because we are using a for loop to iterate through the array
            and we are using a for loop to iterate through the array
            and we are using a variable to store the prefix sum
            and we are using a variable to store the largest sum
            and we are using a return statement to return the largest sum
            and we are using a return statement to return the result
        """
        """ Better Approach - Use 2 nested loops to iterate through the array
            Use Two Pointers to iterate through the array.
            Eliminate the innermost loop by using a variable to store the 
            prefix sum as we iterate through the array. This is done by resetting
            the prefix sum to 0 if it is less than 0.
            Time Complexity: O(n^2)
            Space Complexity: O(1)
            where n is the number of elements in the array
            because we are using a for loop to iterate through the array
            and we are using a variable to store the prefix sum
            and we are using a variable to store the largest sum
            and we are using a return statement to return the largest sum
            and we are using a return statement to return the result
        """
        """ Optimal - Kadane's Algorithm """
        prefix = 0
        largest = float('-inf')

        for num in nums:
            if prefix < 0:
               prefix = 0
            prefix += num
            largest = max(largest, prefix)
        return largest
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # where n is the number of elements in the array
        # because we are using a for loop to iterate through the array
        # and we are using a variable to store the prefix sum
        # and we are using a variable to store the largest sum
        # and we are using a return statement to return the largest sum
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result

        """ Follow Up: Print the subarray with the largest sum """
        start = 0
        end = 0

        for i in range(len(nums)):
            if prefix < 0:
               prefix = 0
            prefix += nums[i]
            if prefix > largest:
                largest = prefix
                end = i
                start = i
        return nums[start:end+1]
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # where n is the number of elements in the array
        # because we are using a for loop to iterate through the array
        # and we are using a variable to store the prefix sum
        # and we are using a variable to store the largest sum
        # and we are using a return statement to return the largest sum
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result

        """ Follow Up: Print the starting and ending index of the subarray with the largest sum """
        start = 0
        end = 0

        for i in range(len(nums)):
            if prefix < 0:
               prefix = 0
            prefix += nums[i]
            if prefix > largest:
                largest = prefix
                end = i
                start = i       
        return start, end
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # where n is the number of elements in the array because we are using a for loop to iterate through the array
        # and we are using a variable to store the prefix sum
        # and we are using a variable to store the largest sum
        # and we are using a return statement to return the starting and ending index of the subarray with the largest sum
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result