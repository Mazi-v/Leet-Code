/*
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
*/
/**
 * @param {number[][]} grid
 * @return {number}
 */

var minPathSum = function (grid) {
  const m = grid.length;
  const n = grid[0].length;
  const result = new Array(m);

  for (let i = 0; i < m; i++) {
    result[i] = new Array(n).fill(0);
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (i === 0 && j === 0) {
        result[i][j] = grid[i][j];
      } else if (i === 0) {
        result[i][j] = grid[i][j] + result[i][j - 1];
      } else if (j === 0) {
        result[i][j] = grid[i][j] + result[i - 1][j];
      } else {
        result[i][j] =
          grid[i][j] + Math.min(result[i - 1][j], result[i][j - 1]);
      }
    }
  }
  return result[m - 1][n - 1];
};
