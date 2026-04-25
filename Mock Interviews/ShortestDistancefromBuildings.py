""" Mock Interview; 24th April, 2026. with Mahima """
"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7

Input: grid = [[1,0]]
Output: 1

Input: grid = [[1]]
Output: -1


"""
from typing import List
from collections import deque

class Solution:
    def findShortestDistance(self, grid: List[List[int]]) -> int:
        shortest = float("inf")
        buildings = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    buildings += 1

        def bfs(r,c):
            count = 0
            path_sum = 0
            queue = deque()
            queue.append((r,c,1))
            visited = set()
            while queue and count <= buildings:
                r, c, dist = queue.popleft()
                directions = [[0,1],[1,0],[-1,0],[0,-1]]

                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col] == 2 or (row, col) in visited:
                         continue
                    visited.add((row, col))
                    if grid[row][col] == 1:
                        count += 1
                        path_sum += dist
                        continue
                    queue.append((row, col, dist + 1))

            if count == buildings:
                return path_sum
            return False

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    distance = bfs(r,c)
                    # print(r,c,distance)
                    if distance:
                        shortest = min(shortest, distance)

        return shortest if shortest != float("inf") else -1

grid = [[1]]
obj = Solution()
print(obj.findShortestDistance(grid))