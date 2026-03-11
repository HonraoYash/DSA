class Solution:
    def longestSubarray(self, nums, k):
        """
        Brute Force - 
        Generate all subarrays, and check if their sum equals K. Keep a track of all such subarrays seen.
        Keep track of the maximum length of such subarrays seen. Return the maximum length seen.
        Time Complexity = O(n^2)
        Space Complexity = O(1)
    
        for i in range(len(nums)):      # Iterate through the array
            prefix = 0
            for j in range(i, len(nums)): # Iterate through the subarray
                for k in range(i, j+1): # Iterate through the subarray
                    prefix += nums[k]
                    if prefix == k:
                        max_length = max(max_length, k-j+1) # Update the maximum length
                    if prefix > k:
                        break
        return max_length
        # Time Complexity: O(n^3)
        # Space Complexity: O(1)
        # where n is the number of elements in the array
        # because we are using a for loop to iterate through the array
        # and we are using a for loop to iterate through the subarray
        # and we are using a variable to store the prefix sum
        # and we are using a variable to store the maximum length
        # and we are using a return statement to return the maximum length
        """
        """
        Better Approach - Eliminate the innermost loop by using a variable to store the 
        prefix sum as we iterate through the array. This is done by resetting
        the prefix sum to 0 if it is less than 0.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        where n is the number of elements in the array
        because we are using a for loop to iterate through the array
        and we are using a for loop to iterate through the subarray
        and we are using a variable to store the prefix sum
        and we are using a variable to store the maximum length
        and we are using a return statement to return the maximum length
        """
        """ Better Approach - Use a hashmap to store the prefix sum and the index of the subarray with the sum equal to K.
        Time Complexity: O(n)
        Space Complexity: O(n)
        where n is the number of elements in the array
        because we are using a for loop to iterate through the array
        and we are using a hashmap to store the prefix sum and the index of the subarray with the sum equal to K
        and we are using a return statement to return the maximum length
        """
        """ This approach is the best optimal solution if the array contains positives and negative elements. """
        preSumMap = {}
        sum = 0
        maxLen = 0

        for i in range(len(nums)):
            sum += nums[i]

            if sum == k:
                maxLen = max(maxLen, i + 1)

            rem = sum - k
            if rem in preSumMap:
                maxLen = max(maxLen, i - preSumMap[rem])

            if sum not in preSumMap:
                preSumMap[sum] = i

        return maxLen
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        # where n is the number of elements in the array
        # because we are using a for loop to iterate through the array
        # and we are using a hashmap to store the prefix sum and the index of the subarray with the sum equal to K
        # and we are using a return statement to return the maximum length
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result
        
        """ Optimal Solution: If the array contains only positive and zero elements.
        If the array contains only positive and zero elements, we can use a two pointer and 
        greedy approach to find the largest subarray with the sum equal to K. 
        """
        left, right = 0, 0
        longest = 0
        sum = nums[0]
        while right < len(nums):
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            if sum == k:
                longest = max(longest, right - left + 1)
            right += 1
            if right < len(nums):
               sum += nums[right]
        return longest
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # where n is the number of elements in the array
        # because we are using a while loop to iterate through the array
        # and we are using a variable to store the sum
        # and we are using a variable to store the longest subarray
        # and we are using a return statement to return the longest subarray
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result

        """ Follow Up: Print the subarray with the largest sum """
        left, right = 0, 0
        longest = 0
        sum = nums[0]
        while right < len(nums):
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            if sum == k:
                longest = max(longest, right - left + 1)
            right += 1  
            if right < len(nums):
               sum += nums[right]
        return nums[left:right+1]

        """ Follow Up: Print the starting and ending index of the subarray with the largest sum """
        left, right = 0, 0
        longest = 0
        sum = nums[0]
        while right < len(nums):
            while left <= right and sum > k:
                sum -= nums[left]
                left += 1
            if sum == k:
                longest = max(longest, right - left + 1)
            right += 1  
            if right < len(nums):  
               sum += nums[right]
        return left, right
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        # where n is the number of elements in the array
        # because we are using a while loop to iterate through the array
        # and we are using a variable to store the sum
        # and we are using a variable to store the longest subarray
        # and we are using a return statement to return the starting and ending index of the subarray with the largest sum
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result

        """ Mention to the interviewer that:
           1) If the array contains positives and negatives, the second 'Better Approach' is the best optimal solution.
           2) But if the array contains only positives and zeros, the third 'Optimal Solution' is the best optimal solution.
        """