from typing import List

class Solution:
    """
    Given an m x n integer matrix with the following properties:

      • Each row is sorted in non-decreasing order.
      • The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return True if target is in the matrix, and False otherwise.

    The solution must run in O(log(m * n)) time complexity.
    """

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix[0]) - 1

        while i < len(matrix) and j >= 0:
            if matrix[i][j] == target:
                return True
            if target > matrix[i][j]:
                i += 1
            else:
                j -= 1

        return False