import sys

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        result = [[0] * n for _ in range(n)]
        directions = [[-1, +1], [-1, 0], [-1, -1]]  # Up-right, Up, Up-left
        
        for i in range(n):
            for j in range(n):
                current_val = matrix[i][j]
                
                if i == 0:
                    result[i][j] = current_val
                else:
                    min_value = sys.maxsize
                    
                    for direction in directions:
                        x = i + direction[0]
                        y = j + direction[1]
                        
                        if 0 <= x < n and 0 <= y < n:
                            min_value = min(result[x][y], min_value)
                    
                    current_val += min_value
                result[i][j] = current_val
        
        ans = min(result[n - 1])
        return ans