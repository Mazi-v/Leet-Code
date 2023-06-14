"""You are given an integer array nums. You want to maximize the number of points you get by performing
 the following operation any number of times:
Pick any nums[i] and delete it to earn nums[i] points. 
Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.
"""
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_val = max(nums)
        
        # Create an array to store the accumulated points for each number
        points = [0] * max_val
        
        # Calculate the accumulated points for each number
        for num in nums:
            if num != 0:
                points[num-1] += num

        max_points = [0] * max_val
        max_points[0] = points[0]
        
        for i in range(1, max_val):
            # Choose the maximum between skipping the current number
            # and adding the current number's points to the maximum points of two steps before
            max_points[i] = max(max_points[i-1], points[i] + (max_points[i-2] if i >= 2 else 0))
        
        # Return the maximum points that can be earned
        return max_points[-1]