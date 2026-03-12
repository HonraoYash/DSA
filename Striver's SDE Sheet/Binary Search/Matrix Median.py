class Solution:
    def findMedian(self, matrix):
        """ Brute Force - 
           Put all the elements of the matrix into a 1D array and sort it.
           Return the middle element of the array.
           Time Complexity - O(n*m*log(n*m))
           Space Complexity - O(n*m)
           where n is the number of rows and m is the number of columns
           because we are using a for loop to iterate through the matrix
           and we are using a for loop to iterate through the array
           and we are using a return statement to return the result
           and we are using a return statement to return the result
           Interviewer not happy with the time complexity.
        """
        """ Optimal Approach - We need to better than O(n*m*log(n*m)) time complexity.
            We need to skip some elements, and since the rows are sorted, it is a hint that we can use binary search.
            So whatever is the middle element, there will be (n*m)/2 elements less than or equal to it.
            [no.of.elements <= median] > (n*m)/2
            We can use this to our advantage to find the median.
            The Search space is between the minimum and maximum elements of the matrix.
            We can use binary search to find the median.
            We can use a helper function to count the number of elements less than or equal to the middle element.
            Example: [[1,5,7,9,11]
                      [2,3,4,5,10]
                      [9,10,12,14,16]]    -> This is the matrix.
                Arranging in a 1D array: [1,2,3,4,5,5,7,9,9,10,10,11,12,14,16] -> 15 elements (Median is 9)
                Array of numbers less than equal to themself:
                                Arr   =  [1,2,3,4,6,6,7,9,9,11,11,12,13,14,15]
                Median is the middle element of the array. 
                So our task will be to use binary search on Arr and find the number which satisfies the condition:
                [no.of.smaller elements <= median] > (n*m)/2 (Has to be strictly greater than (n*m)/2)
                Because for the median, the number of elements less than or equal to the median should be greater than (n*m)/2.
                We take advantage of this fact, and do a Binary Search on the Arr to find the smallest number
                which satisfies the condition, and return the corresponding number from the 1D Array.
        """
        """ Watch Striver's video for better understanding """
        n = len(matrix)
        m = len(matrix[0])

        low = min(matrix[i][0] for i in range(n))
        high = max(matrix[i][m-1] for i in range(n))
        req = (n*m) // 2

        while low <= high:
            mid = (low + high) // 2
            smaller_than_mid = self.helperfunction(matrix, mid)
            if smaller_than_mid > req:
                high = mid - 1
            else: 
                low = mid + 1

        return low

    def helperfunction(self, matrix, mid):
        count = 0
        for i in range(n):
            cnt += self.upper_bound(matrix[i], mid)
        return cnt

    def upper_bound(self, row, n):    # O(nlog(m))
        lo, hi = 0, len(row)
        while lo < hi:
            mid = (lo + hi) // 2
            if row[mid] <= n:
                lo = mid + 1
            else:
                hi = mid
        return lo
        # Time Complexity - O(log(10^9)*n*log(m)) - (10^9 is the maximum value in the matrix)
        # Space Complexity - O(1)
        # where n is the number of rows and m is the number of columns
        # because we are using a for loop to iterate through the matrix
        # and we are using a binary search to find the upper bound
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result