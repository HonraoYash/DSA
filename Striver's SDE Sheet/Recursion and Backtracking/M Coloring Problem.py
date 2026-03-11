from collections import defaultdict

class Solution:
    def graphColoring(self, edges, m, n):
        """ Only one way of solving this problem is by using a recursive function to explore all possible colors."""
        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        color = [0]*n

        def isSafe(node, color):
            for neighbor in adj[node]:
                if color[neighbor] == color:
                    return False
            return True

        def dfs(node):
            if node == n:
                return True

            for i in range(1, m+1):
                if isSafe(node, i):
                    color[node] = i
                    if dfs(node+1):
                        return True
                    color[node] = 0
            return False

        return True if dfs(0) else False
        # Time Complexity: O(m^n)
        # Space Complexity: O(n)
        # where n is the number of nodes and m is the number of colors
        # because we are using a recursive function to explore all possible colors
        # and we are using a for loop to iterate through the colors
        # and we are using a if statement to check if the color is safe
        # and we are using a return statement to return the result
        # and we are using a return statement to return the result