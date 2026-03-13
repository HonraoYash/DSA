class Solution:
    def findPages(self, nums, m):
        """ Brute Force - Do recursion on Dynamic Programming.
            Time Complexity = O(2^n)
            Space Complexity = O(n)
            Don't think of this solution, directly tell the Binary Search Solution.
        """
        """ Optimal Approach - Use Binary Search to find the minimum number of maximum pages allocated to a student.
            The minimum number of pages allocated to any student will the minimum number of pages in the array.
            The maximum number of pages allocated to any student will be the sum of all the pages in the array.
            Therefore, the Search Space is [min(nums), sum(nums)].
            We do a Binary Search on this Search Space to find the minimum number of maximum pages allocated to a student.
            If the consider the mid of this Search Space as a 'Upper Bound' to allocating pages to a student, 
            and use a helper function to check if it is possible to allocate pages to all the students with the given upper bound.
            If it's possible, meaning any 'Upper Bound'  more than that will also be possible and wont be the minimum, hence we 
            eliminate the right half and search in the left half. 
            Whereas on the other hand, if it's not possible to allocate pages to all the students with the given upper bound, 
            we need to increase the upper bound and search in the right half.
            We continue this process until we find the minimum number of maximum pages allocated to a student.
            Return the minimum number of maximum pages allocated to a student.
        """
        low = min(nums)
        high = sum(nums)
        res = None

        while low <= high:                 # O(log(sum(nums))
            mid = (low+high) // 2
            if self.isPossible(nums, m, mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res

    # To check that if it is possible to allocate pages to all the students with the given upper bound.
    def isPossible(self, nums, m, barrier): # O(N)
        pages = 0
        students = 1

        for i in range(len(nums)):
            if nums[i] > barrier:
                return False

            if pages + nums[i] > barrier:
                students += 1
                pages = nums[i]
            else:
                pages += nums[i]

        if students <= m:
            return True
        return False
    # Total Time Complexity = O(N*log(sum(nums)))
    # Total Space Complexity = O(1)
    # where N is the number of books and sum(nums) is the total number of pages

obj = Solution()
nums = [25, 46, 28, 49, 24] 
m=4
print(obj.findPages(nums, m))