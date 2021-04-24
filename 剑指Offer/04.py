# Find target number in a 2D matrix.
# The number in matrix increases from left to right.
# The number in matrix increases from top to bottom.
# Tip: Find a beginning point where the numbers at one direction increase and the other decrease.

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        
        i, j = len(matrix) - 1, 0

        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] < target:
                j+=1
            elif matrix[i][j] > target:
                i-=1
            else:
                return True
        return False
