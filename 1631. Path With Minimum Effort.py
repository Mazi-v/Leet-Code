# You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, 
# (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

from typing import List
from heapq import heappop, heappush

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        visited = set()
        min_heap = [(0, 0, 0)]  # (diff, row, col)
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while min_heap:
            diff, r, c = heappop(min_heap)
            if (r, c) in visited:
                continue
            if r == rows - 1 and c == cols - 1:
                return diff
            visited.add((r, c))
            for x, y in dirs:
                new_r, new_c = r + x, c + y
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                    new_diff = max(diff, abs(heights[new_r][new_c] - heights[r][c]))
                    heappush(min_heap, (new_diff, new_r, new_c))
