"""You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest."""
import queue
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        a=[]
        priority_queue = queue.PriorityQueue()

        counter=0
        for i in range (len(mat)):
            count=0
            for j in range(len(mat[0])):
                if (mat[i][j]==0):
                    break
                count+=1    
            a.append([count,i])
            priority_queue.put((count,i))
        
        ans=[]
        while priority_queue and k >0  :
            k-=1
            count, row = priority_queue.get()
            ans.append(row)
        return ans
