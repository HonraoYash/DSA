class Solution:
    def canPlaceCows(self, nums, cows, distance):
        last = nums[0]
        cows_placed = 1
        for i in range(1, len(nums)):
            if nums[i] - last >= distance:
                cows_placed += 1
                last = nums[i]
        if cows_placed >= cows:
            return True
        return False

    def aggressiveCows(self, nums, k):
        """ Brute Force - Use a Greedy Approach to place the cows in the stalls. 
        nums.sort()
        low = 1                      
        high = max(nums) - min(nums)
        for i in range(low, high+1):
            if self.canPlaceCows(nums, k, i):
                continue
            else:
                return i - 1

        # Time Complexity - O(max-min)*O(N) - (max-min) is the search space and O(N) is the time taken to place the cows in the stalls.
        # Space Complexity - O(1) - because we are not using any extra space.
        # Interviewer not happy with the time complexity.
        """
        """ Optimal Approach - Let's try to use Binary Search to find the maximum distance between the cows. 
            The search space is [1, max(nums) - min(nums)].
            We do a Binary Search on this Search Space to find the maximum distance between the cows.
            If the consider the mid of this Search Space as a 'Distance' between the cows, 
            and use a helper function to check if it is possible to place the cows in the stalls with the given distance.
            If it's possible, meaning any 'Distance' more than that will also be possible and wont be the maximum, hence we 
            eliminate the right half and search in the left half. 
            Whereas on the other hand, if it's not possible to place the cows in the stalls with the given distance, 
            we need to decrease the distance and search in the right half.
            We continue this process until we find the maximum distance between the cows.
            Return the maximum distance between the cows.
        """
        nums.sort()
        low = 0
        high = nums[-1] - nums[0]

        while low <= high:
            mid = (low + high) // 2
            if self.canPlaceCows(nums, k, mid):
                low = mid + 1
            else:
                high = mid - 1

        return high
        # The answer will always be at high, because at start low is possible and high is not possible.
        # But after binary search, they change the duality.
        # Time Comlpexity - O(NlogN) + O(log(max-min)) * O(N)
        # Space Complexity - O(1)