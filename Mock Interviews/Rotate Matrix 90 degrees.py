""" Mock Interview with Mahima: 10th April, 2026 """
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

"""
from typing import List

class Solution:
    def rotateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        # Step 1: Swap the rows of the matrix across the center row.
        for row in range(rows//2):
            matrix[row], matrix[rows - row - 1] = matrix[rows - row - 1], matrix[row]
        
        # Step 2: Swapping the elements across the diagonal of the matrix
        for row in range(rows):
            for col in range(row+1, rows):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col] 
                
        return matrix
        # Time Complexity - O(N^2)
        # Space Complexity - O(1)
    
matrix = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.rotateMatrix(matrix))