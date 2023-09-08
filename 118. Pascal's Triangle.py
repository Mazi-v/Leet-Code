"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]  
        if numRows == 0:
            return [[]] 
        for row in range(0,numRows):
            temp = [1]* (row+1)
            for index in range(1,len(temp)):
                if index ==len(temp)-1:
                    continue
                else :
                    pre = result[row-1]
                    temp[index]=(pre[index]+pre[index-1]) 
            result.append(temp.copy())   
        return result         

        