class Solution(object):
    def rob(self, nums):
        """
        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed. All houses at this place are arranged in a circle.
        That means the first house is the neighbor of the last one. 
        Meanwhile, adjacent houses have a security system connected, 
        and it will automatically contact the police if two adjacent houses were broken into on the same night.
        Given an integer array nums representing the amount of money of each house, 
        return the maximum amount of money you can rob tonight without alerting the police.        
        """
        if len(nums) == 1:
            return nums[0]  # Base case: Only one house, return the amount in that house

        # Calculate the maximum amount by considering both scenarios:
        # 1. Robbing from the second house to the last house
        # 2. Robbing from the first house to the second to last house
        return max(self.maxRob(nums[1:]), self.maxRob(nums[:-1]))

    def maxRob(self, nums):
        temp, curr, pre = 0, 0, 0

        # Iterate through the houses and calculate the maximum amount that can be stolen
        for i in range(len(nums)):
            if pre + nums[i] > curr:
                temp = curr
                curr = pre + nums[i]
                pre = temp
            else:
                pre = curr

        return curr  # Return the maximum amount that can be stolen