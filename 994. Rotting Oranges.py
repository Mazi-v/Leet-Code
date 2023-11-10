"""You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1."""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        total_fresh_oranges = 0
        rottens = []

        # Iterate through the grid to count fresh oranges and find rotten oranges
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    total_fresh_oranges += 1
                if grid[i][j] == 2:
                    rottens.append((i, j))

        # If there are no fresh oranges initially, return 0
        if total_fresh_oranges == 0:
            return 0

        # Initialize a queue for BFS, directions for adjacent cells, and time counter
        queue = deque()
        direction = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        minutes = 0
        
        # Initialize a matrix to mark visited cells
        visited = [[False] * col for _ in range(row)]

        # Add initial rotten oranges to the queue and mark them as visited
        for rotten in rottens:
            queue.append((rotten[0], rotten[1]))
            visited[rotten[0]][rotten[1]] = True

        # Perform BFS to simulate the rotting process
        while queue:
            size = len(queue)
            # Process oranges at the current time level
            for _ in range(size):
                curr_x, curr_y = queue.popleft()
                # Check adjacent cells and update fresh oranges
                for x, y in direction:
                    new_x, new_y = curr_x + x, curr_y + y
                    # Check bounds and if the cell is not visited
                    if 0 <= new_x < row and 0 <= new_y < col and not visited[new_x][new_y]:
                        # Mark the cell as visited
                        visited[new_x][new_y] = True
                        # If the cell has a fresh orange, update its status and add to the queue
                        if grid[new_x][new_y] == 1:
                            grid[new_x][new_y] = 2
                            total_fresh_oranges -= 1
                            # If there are no more fresh oranges, return the time
                            if total_fresh_oranges == 0:
                                return minutes + 1
                            queue.append((new_x, new_y))
            # Increment the time counter for the next level
            minutes += 1

        # If there are still fresh oranges left, return -1 (impossible)
        return -1