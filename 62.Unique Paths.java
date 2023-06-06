/*There is a robot on an m x n grid. The robot is initially located at the top-left corner.
The robot tries to move to the bottom-right corner.
 The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.*/
class Solution {
    public int uniquePaths(int m, int n) {
 
        int count[][] = new int[m][n];
        
        for (int i = 0 ; i < m ; i++){
            for (int j = 0 ; j < n ; j++){
                if ( i==0||j==0){
                    count[i][j]=1;
                }
                else{
                count[i][j]= count[i-1][j]+count[i][j-1];
                }
            }
        }
       return count[m-1][n-1];

        }
    }