class Solution:
    def findPath(self, grid):
        #your code goes here
        """ Only one way of solving this problem is by using a recursive function to explore all possible paths."""
        n = len(grid)
        res = []
        vis = [[0]*n for _ in range(n)]
        di = [1,0,0,-1]
        dj = [0,-1,1,0] 

        if grid[0][0] == 1:
           self.backtrack(0,0,"",vis,res,grid,di,dj,n)
        return res

    def backtrack(self, i,j,track,vis,res,grid,di,dj,n):
        if i==n-1 and j==n-1:
            res.append(track)
            return
        
        string = "DLRU"
        vis[i][j] = 1
        for k in range(4):
            nexti = i + di[k]
            nextj = j + dj[k]
            if (nexti >=0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and grid[nexti][nextj] == 1):
                self.backtrack(nexti,nextj,track+string[k],vis,res,grid,di,dj,n)
        vis[i][j] = 0
        # Time Complexity: O(4^(n*m))
        # Space Complexity: O(n*m)
        # where n is the number of rows and m is the number of columns
        # because we are using a recursive function to explore all possible paths
        # and we are using a visited matrix to keep track of the cells we have visited
        # and we are using a string to keep track of the path we have taken
        # and we are using a list to store the result
        # and we are using a list to store the result
n = 2 
grid = [ [1, 0] , [1, 0] ]
obj = Solution()
print(obj.findPath(n, grid))