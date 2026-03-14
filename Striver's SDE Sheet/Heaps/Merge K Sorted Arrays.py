import heapq

class Solution:
    def mergeKSortedArrays(self, arr, k):
        """ Brute Force - Iterate through the 2d array and push all the elements into a heap.
            Then, pop the smallest element from the heap and add it to the result array.
            # Time Complexity = O(k^2 * log(k))
            # Space Complexity = O(k^2)
            # where k is the number of arrays and n is the number of elements in each array
            # because we are using a for loop to iterate through the arrays
            # and we are using a for loop to iterate through the elements of the arrays
            # and we are using a heap to store the elements of the arrays
            # and we are using a return statement to return the result
            # and we are using a return statement to return the result
        """
        # heap = [arr[i][j] for i in range(k) for j in range(k)]
        # heapq.heapify(heap)                          

        # res = []
        # while heap:
        #     res.append(heapq.heappop(heap))
        # return res
        """ Optimal Solution - Min Heap of size k
        
            Key Idea: Instead of pushing all elements into the heap upfront, we only push
            the first element of each array initially. The heap always holds exactly one
            element per array at a time, so its size never exceeds k.

            At each step:
            - Pop the smallest element from the heap → add to result
            - Push the next element from the same array (if it exists)

            Since arrays are already sorted, the next smallest element globally must be
            either the current minimum in the heap or the next unvisited element in the
            same array — so we never miss any element.

            We store (value, array_index, element_index) in the heap so we know
            which array to pull the next element from after each pop.

            Example: arr = [[1,3,5], [2,4,6], [0,7,8]], k = 3
            - Init heap: [(1,0,0), (2,1,0), (0,2,0)]
            - Pop (0,2,0) → res=[0], push (7,2,1)
            - Pop (1,0,0) → res=[0,1], push (3,0,1)
            - Pop (2,1,0) → res=[0,1,2], push (4,1,1)
            - ... and so on until heap is empty

            Time  - O(k log k) to init heap + O(k² log k) for k² pops = O(k² log k)
            Space - O(k)  ← heap holds exactly one element per array at any time
        """
        # Push (value, array_index, element_index) for first element of each array
        heap = []
        for i in range(k):
            heapq.heappush(heap, (arr[i][0], i, 0))   # O(k log k)

        res = []
        while heap:                                     # O(k² log k)
            val, i, j = heapq.heappop(heap)
            res.append(val)

            if j + 1 < k:                              # push next element from same array
                heapq.heappush(heap, (arr[i][j+1], i, j+1))

        return res

arr = [[1,5,9], [10,11,13], [12,13,15]]
k = 3

arr = [[1,2,3],[4,5,6],[7,8,9]]
k = 3

arr = [[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]]
k = 4

obj = Solution()
print(obj.mergeKSortedArrays(arr, k))