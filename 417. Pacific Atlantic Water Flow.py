"""There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans."""
class Solution:
    def bfs(self, heights: List[List[int]], q: deque, visited: set):
        col = len(heights[0])
        row = len(heights)
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while q:
            curr = q.popleft()
            i = curr[0]
            j = curr[1]
            for x, y in directions:
                nx, ny = x + i, y + j
                if (not 0 <= nx < row) or (not 0 <= ny < col) or (nx, ny) in visited or heights[nx][ny] < heights[i][j]:
                    continue
                visited.add((nx, ny))
                q.append((nx, ny))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        col = len(heights[0])
        row = len(heights)
        # Initialize sets to track visited cells for the Pacific and Atlantic oceans
        visitedP = set()
        visitedA = set()
        # Initialize queues for BFS traversal starting from Pacific and Atlantic oceans
        pq = deque()
        aq = deque()
        # Start BFS traversal from the left and right boundaries (Pacific and Atlantic oceans)
        for i in range(row):
            pq.append((i, 0))
            aq.append((i, col - 1))
            visitedP.add((i, 0))
            visitedA.add((i, col - 1))
        for j in range(col):
            pq.append((0, j))
            aq.append((row - 1, j))
            visitedP.add((0, j))
            visitedA.add((row - 1, j))
        # Perform BFS from both oceans
        self.bfs(heights, pq, visitedP)
        self.bfs(heights, aq, visitedA)
        # Find the intersection of visited cells in both oceans
        return list(visitedP & visitedA)