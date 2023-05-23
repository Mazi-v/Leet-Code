class Solution {
    /*
     * Given an m x n 2D binary grid grid which represents a map of '1's (land) and
     * '0's (water),
     * return the number of islands.
     * An island is surrounded by water and is formed by connecting adjacent lands
     * horizontally or vertically.
     * You may assume all four edges of the grid are all surrounded by water.
     */
    public int numIslands(char[][] grid) {

        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    land(grid, i, j);

                    count++;
                }
            }

        }
        return count;
    }

    public void land(char[][] grid, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] != '1') {
            return;
        }

        grid[i][j] = '&';

        land(grid, i + 1, j);
        land(grid, i - 1, j);
        land(grid, i, j - 1);
        land(grid, i, j + 1);
    }

}