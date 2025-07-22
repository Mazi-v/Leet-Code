"""You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r)."""
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        start = 0
        nums_set = set()
        temp_sum = 0
        for end in range(len(nums)):
            if nums[end] in nums_set:
                while nums[end] in nums_set:
                    nums_set.remove(nums[start])
                    temp_sum-=nums[start]
                    start+=1
                    
            nums_set.add(nums[end])
            temp_sum+=nums[end]
            res = max(res,temp_sum)
        return res

