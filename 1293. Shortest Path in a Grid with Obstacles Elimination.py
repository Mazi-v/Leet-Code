
from collections import deque
from typing import List
class Solution:
    """
    Returns the minimum number of steps to walk from the upper-left corner
    to the lower-right corner of the grid, given that you can eliminate at most k obstacles.
    If not possible, returns -1.
    """
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        q= deque()
        q.append((0,0,grid[0][0])) # (row, col, obstacles_used)
        step = 0
        res = [[float("inf")]*m for _ in range(n)]
        res[0][0] = grid[0][0]
        
        while q:
            size = len(q)
            for _ in range(size):
                curr_x, curr_y, used = q.popleft()
                if  used > k:continue
                if  curr_x == n-1 and curr_y == m-1: return step
                for dx , dy in directions: 
                    x , y = curr_x + dx , curr_y + dy
                    if 0<=x<n and 0<=y<m:
                        new_used = used + grid[x][y]
                        if new_used < res[x][y]:
                            res[x][y] = new_used
                            q.append((x,y,new_used))

            step+=1
        return -1
