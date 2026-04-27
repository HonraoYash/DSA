""" Mock Interview; 26th April, 2026. with Hitha """
""" Given an m x n binary grid grid where:

1 represents a person’s home
0 represents an empty cell

Return the minimum total travel distance for all people to meet at a single point.

The distance between two points (x1, y1) and (x2, y2) is the Manhattan Distance:

∣x1−x2∣+∣y1−y2∣

You may choose any cell in the grid as the meeting point. 

grid = [
  [1,0,0,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]

o/p: 6
"""
from typing import List

class Solution:
    def minTotalDistance(self, grid: List[List[int]]):
        houses = []
        minimumTotalDistance = float("inf")
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    houses.append([r,c])
        
        def getTotalDistance(r,c):
            distance = 0
            for house in houses:
                row, col = house
                distance += abs(r - row) + abs(c - col)
            return distance
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                distance = getTotalDistance(r,c)
                minimumTotalDistance = min(minimumTotalDistance, distance)
        return minimumTotalDistance
        # Time Complexity - O((m*n)^2)

        # Approach 2:
        # houses = []
        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             houses.append([r,c])

        # if len(houses) == 1:
        #     return 0
        # X, Y = houses[0][0], houses[0][1]

        # for i in range(1,len(houses)):
        #     X = (houses[i][0] + X) // 2


grid = [
  [1,0,0,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]
obj = Solution()
print(obj.minTotalDistance(grid))