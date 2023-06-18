"""You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells."""
class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mod = 10 ** 9 + 7
        
        # Create resultArray to store the computed path counts for each cell
        resultArray = [[0] * len(grid[0]) for _ in range(len(grid))] 

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Calculate the count of strictly increasing paths for each cell
                ans = (ans + self.cellPathCount(i, j, grid, resultArray)) % mod

        return ans

    def cellPathCount(self, i, j, grid, resultArray):
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        mod = 10 ** 9 + 7

        # If the path count for the current cell has already been computed, return it
        if resultArray[i][j] != 0:
            return resultArray[i][j]

        ans = 1
        for d in direction:
            x = i + d[0]
            y = j + d[1]
            # Check if the adjacent cell is within bounds and has a smaller value
            if (
                0 <= x < len(grid) and
                0 <= y < len(grid[0]) and
                grid[i][j] < grid[x][y]
            ):
                # Recursively calculate the path count for the adjacent cell
                ans += self.cellPathCount(x, y, grid, resultArray)
                ans %= mod

        resultArray[i][j] = ans
        return ans