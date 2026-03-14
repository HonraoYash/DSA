import heapq

class Solution:
    def maxSumCombinations(self, nums1, nums2, k):
        """ Brute Force - Use two for nested loops to iterate through the arrays and calculate the sum of the combinations of the elements.
            Store the sum of the combinations in a list. Sort the list and return the last k elements.
            Time Complexity = O(n^2)
            Space Complexity = O(n^2)
        """
        # res = []
        # for num1 in nums1:
        #     for num2 in nums2:
        #         res.append(num1 + num2)
        # res.sort()
        # return res[-k:][::-1]
        """ Optimal Approach - Max Heap + Visited Set
    
            Key Idea: Sort both arrays in descending order. The largest possible sum is always
            nums1[0] + nums2[0]. The next candidates can only be (i+1, j) or (i, j+1) — moving
            one step right in either array. This is because both arrays are sorted, so the next
            best sum must come from a neighboring index pair.

            We use a max heap to always extract the current largest sum, and a visited set to
            avoid pushing the same index pair (i,j) twice into the heap.

            At each step:
            - Pop the largest sum from the heap → add to result
            - Push its two neighbors (i+1,j) and (i,j+1) into the heap if not visited

            We repeat this k times, and each pop gives us the next largest combination.
            The visited set ensures we never process the same pair twice.

            Example: nums1=[5,4,1], nums2=[6,3,2], k=3
            - Start: heap=[(5+6, 0,0)=11]
            - Pop (11,0,0) → res=[11], push (4+6=10,1,0) and (5+3=8,0,1)
            - Pop (10,1,0) → res=[11,10], push (1+6=7,2,0) and (4+3=7,1,1)
            - Pop (8,0,1)  → res=[11,10,8] ✓

            Time  - O(N log N + k log k)  (sorting both arrays + k heap operations)
            Space - O(N + k)              (visited set + heap, both grow at most 2k)
        """
        if not nums1 or not nums2:      # empty list check
            return []
        k = min(k, len(nums1) * len(nums2))   # k can't exceed total combinations

        nums1.sort(reverse=True)
        nums2.sort(reverse=True)
        heap = [(-(nums1[0] + nums2[0]), 0, 0)]
        res = []
        visited = set()
        while len(res) < k:
            val, i, j = heapq.heappop(heap)
            res.append(-val)

            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(heap, (-(nums1[i+1] + nums2[j]), i+1, j))
                visited.add((i+1,j))

            if j + 1 < len(nums2) and (i, j+1) not in visited:
                heapq.heappush(heap, (-(nums1[i] + nums2[j+1]), i, j+1))
                visited.add((i, j+1))

        return res

nums1 = [3, 4, 5]
nums2 = [2, 6, 3]
k = 2
obj = Solution()
print(obj.maxSumCombinations(nums1, nums2, k))