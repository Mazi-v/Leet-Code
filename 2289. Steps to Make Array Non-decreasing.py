"""You are given a 0-indexed integer array nums. In one step, remove all elements nums[i] where nums[i - 1] > nums[i] for all 0 < i < nums.length.

Return the number of steps performed until nums becomes a non-decreasing array."""
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack=[]
        result=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            while len(stack)>0 and num>stack[-1][1]:
                a=stack.pop()
                index=a[0]
                val=a[1]
                result[i]=max(result[i]+1,result[index])
                
            else:
                stack.append([i,num])  
        return max(result)        
                


        