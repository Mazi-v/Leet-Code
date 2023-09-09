"""You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise."""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        result = [False]*len(nums)
        result[len(nums)-1]=True
        for i in range (len(nums)-2,-1,-1):
            num=nums[i]
            if num+i>=len(nums):
                result[i]=True
            else:
                while num+i<len(nums) and num >0:
                    if result[num+i]:
                        result[i]= True
                        break
                    num-=1    
              
        return result[0]    