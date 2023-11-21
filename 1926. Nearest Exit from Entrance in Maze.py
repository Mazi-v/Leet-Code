"""You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        # Function to check if a cell is an exit
        def is_exit(i:int, j:int):
            if (i == row_count - 1 or j == col_count - 1 or i == 0 or j == 0) and maze[i][j] != "+":
                return True
            return False
        
        # Function to check if a cell is a valid empty cell
        def is_valid_cell(i: int, j: int):
            if 0 <= i < row_count and 0 <= j < col_count and maze[i][j] == ".":
                return True
            return False
        
        # Count rows and columns in the maze
        row_count = len(maze)
        col_count = len(maze[0])
        
        # Possible movement directions: right, down, up, left
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        
        # Track visited cells
        visited = [[False]*col_count for _ in range(row_count)]
        
        # Queue for BFS (using deque)
        queue = deque()
        queue.append(entrance)  # Add the entrance cell to the queue
        visited[entrance[0]][entrance[1]] = True  # Mark the entrance cell as visited
        
        steps = 0  # Initialize steps counter
        
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()  # Get the current cell from the queue
                curr_x, curr_y = current[0], current[1]  # Extract row and column of the current cell
                
                # Check if the current cell is an exit and not the entrance
                if is_exit(curr_x, curr_y) and current != entrance:
                    return steps  # Return the number of steps if an exit is found
                
                # Explore all possible directions from the current cell
                for direction in directions:
                    next_x = direction[0] + curr_x  # Calculate next row
                    next_y = direction[1] + curr_y  # Calculate next column
                    
                    # Check if the next cell is a valid empty cell and not visited
                    if is_valid_cell(next_x, next_y) and not visited[next_x][next_y]:
                        queue.append([next_x, next_y])  # Add the valid cell to the queue
                        visited[next_x][next_y] = True  # Mark the cell as visited
            
            steps += 1  # Increment steps after exploring all cells at the current distance level
        
        return -1  # Return -1 if no exit is found within the maze