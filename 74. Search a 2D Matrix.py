"""You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity."""
class Solution:
    def searchRow(self,s:int,e:int,target:int,matrix:List[int])->bool:
        mid= (e+s)//2
        if s>e :
            return False
        if matrix[mid]==target:
            return True
        if matrix[mid]>target:
            return self.searchRow(s,mid-1,target,matrix)
        if matrix[mid]<target:
            return self.searchRow(mid+1,e,target,matrix)


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0;j=0
        m=len(matrix[0])-1
        for i in range (len(matrix)):
            x=matrix[i][0]
            y=matrix[i][m]
            if target >=x and target <=y :
                if self.searchRow (0,m,target,matrix[i]):
                    return True
        return False     



        
