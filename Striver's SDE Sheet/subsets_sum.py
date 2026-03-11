class Solution:
    def isSubsetSum(self, arr, target):
        """ The number of subsets of a set is 2^n """
        """ Whenever there is a problem related to array and we have to figure out combinations, 
            we always follow the 'Pick' or 'Not Pick' procedure.
        """
        """ Using Backtracking """
        m = len(arr)
        
        def dfs(i, track, add):
            if add == target:
                return True
            elif i >= m or add > target:
                return False
 
            if dfs(i+1, track, add):
                return True
            track.append(arr[i])
            if dfs(i + 1, track, add + arr[i]):
                return True
            track.pop()

            return False

        track = []

        if dfs(0, track, 0):
            return True
        # Time Complexity - O(N * 2^N) (branching factor is 2 - include and exclude)
        # Space Complexity - O(N)  (Auxiliary space of N needed at worst case to store all elements in arr) 
        # + O(N*2^N)(for storing output)

        """ Follow Up: Print all subsets with sum equal to target """
        res = []

        def dfs(i, track, add):
            if add == target:
                res.append(track.copy())
                return
            elif i >= m or add > target:
                return

            dfs(i+1, track, add)
            track.append(arr[i])    
            if dfs(i + 1, track, add + arr[i]):
                return True
            track.pop()

            return False

        dfs(0, track, 0)
        return res
        # Time Complexity - O(N * 2^N) (branching factor is 2 - include and exclude)
        # Space Complexity - O(N)  (Auxiliary space of N needed at worst case to store all elements in arr) 
        # + O(N*2^N)(for storing output)
        """ Follow Up: Print all subsets in sorted order """
        res.sort()
        return res
        # Time Complexity - O(N * 2^N) (branching factor is 2 - include and exclude)
        # Space Complexity - O(N)  (Auxiliary space of N needed at worst case to store all elements in arr) 
        # + O(N*2^N)(for storing output)

        """ Another Approach: Using Iterative Approach """
        res = []
        for i in range(2**m):
            track = []
            for j in range(m):
                if i & (1 << j):
                    track.append(arr[j])
            res.append(track)
        return res
        # Time Complexity - O(N * 2^N) (branching factor is 2 - include and exclude)
        # Space Complexity - O(N)  (Auxiliary space of N needed at worst case to store all elements in arr) 
        # + O(N*2^N)(for storing output)
        """ Another Approach: Using Dynamic Programming """
        dp = [[False]*(target+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = True
        for i in range(1, m+1):
            for j in range(1, target+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m][target] 
        # Time Complexity - O(N * target)
        # Space Complexity - O(N * target)
        # where N is the number of elements in the array and target is the target sum
        # because we are using a 2D array to store the results of the subproblems
        # and we are using a for loop to iterate through the array
        # and we are using a for loop to iterate through the target sum
        # and we are using a if statement to check if the current element is less than or equal to the target sum
        # and we are using a or statement to check if the current element is less than or equal to the target sum
        # and we are using a else statement to check if the current element is greater than the target sum
        # and we are using a return statement to return the result