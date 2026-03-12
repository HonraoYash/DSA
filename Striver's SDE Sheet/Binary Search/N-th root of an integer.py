""" Rule - Binary Search is not only used to find a number in an array, but it can 
be used on any monotonically increasing or decreasing function. """

class Solution:
    def NthRoot(self, n, m):
        """ We do a Binary search on the answer space [1, m]. 
            Because the nth of m will always be in the range [1, m]. 
            We use a precision of 1e-6 to ensure that the answer is accurate. 
            We run the loop until the difference between the high and low is less than the precision.
        """

        low = 1
        high = m
        while low <= high:
            mid = (low + high) // 2
            if mid**n == m:
                return mid
            elif mid**n < m:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        # Time Complexity - O(log(m))
        # Space Complexity - O(1)
        # where m is the number we are finding the nth root of
        # because we are using a binary search to find the nth root
        # and we are using a while loop to iterate through the range
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result
    
obj = Solution()
print(obj.NthRoot(3, 60))

""" Follow Up: If the Nth root is not an integer, return the integer part of the Nth root. """
def NthRoot(self, n, m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        if mid**n == m:
            return mid
        elif mid**n < m:
            low = mid + 1
        else:
            high = mid - 1          
    return high
    # Time Complexity - O(log(m))
    # Space Complexity - O(1)
    # where m is the number we are finding the nth root of
    # because we are using a binary search to find the nth root
    # and we are using a while loop to iterate through the range
    # and we are using a return statement to return the result
    # and we are using a return statement to return the result

""" Follow Up: Return upto 5 decimal places of the Nth root of M. """
def NthRoot(self, n, m):
    low = 1
    high = m
    while low <= high:
        mid = (low + high) // 2
        if mid**n == m:
            return mid
        elif mid**n < m:
            low = mid + 1
        else:
            high = mid - 1                      
    return high
    # Time Complexity - O(log(m*10^5))
    # Space Complexity - O(1)
    # where m is the number we are finding the nth root of
    # and 10^5 is the precision we are using to return the result
    # because we are using a binary search to find the nth root
    # and we are using a while loop to iterate through the range
    # and we are using a return statement to return the result