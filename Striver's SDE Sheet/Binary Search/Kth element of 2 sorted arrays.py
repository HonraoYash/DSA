class Solution:
    def kthElement(self, a, b, k):
        """ Naive Solution - Use a Min Heap to store the k largest elements of both the arrays.
            Put the first k elements of both the arrays into the heap.
            Return the kth element from the heap.
            Time Complexity = O(klog(k))
            Space Complexity = O(k)
        """
        """ Brute Force - 
            Use 2 pointers to iterate through both the arrays and keep a counter.
            Increment the pointer of the array with the smaller element and increment the counter.
            When the counter reaches k, return the element at the pointer of the array with the smaller element.
            Time Complexity = O(k)
            Space Complexity = O(1)
        """
        """ Optimal Approach - 
            Use Binary Search to find the kth element. 
            Approach is similar to the median of two sorted arrays problem.
            Use 4 pointers l1,r1 for arr1 and l2,r2 for arr2.
            Perform binary search until all l1 > r2 and l2 > r1.
            Choose l1 ad l2 such that l1 + l2 = k.
        """
        A, B = a, b
        if len(A) < len(B):
            A, B = B, A

        low, high = 0, len(A) - 1
        while True:
            i = (low + high) // 2  # Mid element of A
            j = k - i - 2          # Remaining elements from B (subtracting 2 because of the zero order- two zeros from A and B)

            Aleft = A[i] if i>= 0 else float("-inf") # Left element of A
            Aright = A[i+1] if i+1 < len(A) else float("inf") # Right element of A
            Bleft = B[j] if j >= 0 else float("-inf") # Left element of B
            Bright = B[j+1] if j+1 < len(B) else float("inf") # Right element of B

            if Aleft <= Bright and Bleft <= Aright: # If the left elements of A and B are less than the right elements of A and B
                return max(Aleft, Bleft)
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1
        # Time Complexity = O(log(min(n, m)))
        # Space Complexity = O(1)
        # where n is the length of A and m is the length of B
        # because we are using a binary search to find the kth element
        # and we are using a while loop to iterate through the range
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result

a = [100, 112, 256, 349, 770]
b = [72, 86, 113, 119, 265, 445, 892]
k = 7     
obj = Solution()
print(obj.kthElement(a, b, k))