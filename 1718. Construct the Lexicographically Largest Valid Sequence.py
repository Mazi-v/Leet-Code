"""Given an integer n, find a sequence with elements in the range [1, n] that satisfies all of the following:

The integer 1 occurs once in the sequence.
Each integer between 2 and n occurs twice in the sequence.
For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.
The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5."""

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0]
        size = n*2 -1
        def helper(temp,n_set,index):
            if res[0]!=0 :return 
            if len(n_set)==n:
                res[0] = temp
                return 
            while index < size and temp[index] != -1:
                index += 1
            if index >= size:
                return
            for i in range(n,0,-1):
                if i in n_set:continue
                if i==1 :
                    new_temp = temp[:]
                    new_temp[index] = i      
                    helper(new_temp, n_set |set([i]),index+1)
                elif i != 1 and i + index < len(temp) and temp[index] == -1 and temp[index + i] == -1:
                    new_temp = temp[:]
                    new_temp[index] = i
                    new_temp[index+i] = i
                    helper(new_temp, n_set | {i}, index+1)

                
        helper([-1]*size,set(),0)
        return res[0]


