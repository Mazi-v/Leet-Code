"""You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
"""
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == 1:
                continue
            if i + 2 >= n:
                return -1
            # Flip current and next two elements
            nums[i] ^= 1
            nums[i + 1] ^= 1
            nums[i + 2] ^= 1
            count += 1

        return count