from typing import List

class Solution:
    """
    Given an m x n binary matrix grid, where 1 represents land and 0 represents water,
    an island is a group of 1's connected 4-directionally (up, down, left, right).
    
    The area of an island is the number of land cells in it.
    
    Return the maximum area of an island in the grid. If there is no island, return 0.
    """

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0

        def dfs(i: int, j: int) -> int:
            if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) or grid[i][j] == 0 or (i, j) in visited:
                return 0
            visited.add((i, j)) 
            return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    curr_area = dfs(i, j)
                    max_area = max(max_area, curr_area)

        return max_area
