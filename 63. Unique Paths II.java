/*You are given an m x n integer array grid. There is a robot initially located at the top-left corner.
The robot tries to move to the bottom-right corner.
The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. 
A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
*/
class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int[][] res = new int[m][n];

        if (obstacleGrid[0][0] == 1) {
            return 0; // If the starting cell is an obstacle, there is no valid path
        }

        res[0][0] = 1; // There is only one way to reach the starting position

        // Fill in the first row of the matrix
        for (int i = 1; i < n; i++) {
            // If the current cell is a valid path and the previous cell in the row has a
            // valid path, set it to 1
            res[0][i] = (obstacleGrid[0][i] == 0 && res[0][i - 1] == 1) ? 1 : -1;
        }

        // Fill in the first column of the matrix
        for (int i = 1; i < m; i++) {
            // If the current cell is a valid path and the cell above it has a valid path,
            // set it to 1
            res[i][0] = (obstacleGrid[i][0] == 0 && res[i - 1][0] == 1) ? 1 : -1;
        }

        // Fill in the remaining cells of the matrix
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    res[i][j] = -1; // If the current cell is an obstacle, set it to -1
                    continue;
                }

                // If the cells above and to the left are valid paths, add the number of paths
                // from those cells
                if (res[i - 1][j] != -1 && res[i][j - 1] != -1) {
                    res[i][j] = res[i][j - 1] + res[i - 1][j];
                } else {
                    // If either the cell above or the cell to the left is an obstacle, assign the
                    // number of paths from the valid direction
                    res[i][j] = (res[i - 1][j] == -1) ? res[i][j - 1] : res[i - 1][j];
                }
            }
        }

        int ans = (res[m - 1][n - 1] == -1) ? 0 : res[m - 1][n - 1]; // if the result is -1 set it to zero

        return ans; // Return the result
    }
}