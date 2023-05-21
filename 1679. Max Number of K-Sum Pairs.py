class Solution(object):
    """
    You are given an integer array nums and an integer k.

    In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

    Return the maximum number of operations you can perform on the array.
    """
    def maxOperations(self, nums, k):

        # Initialize two pointers, 'i' and 'j', at the start and end of the sorted array
        j, i = len(nums) - 1, 0
        
        nums.sort()
        count = 0
    
        # Iterate until the pointers meet or cross each other
        while i < j:
            # If the sum of the numbers at 'i' and 'j' is equal to 'k'
            if nums[i] + nums[j] == k:
                # Increment the counter and move the pointers towards the center
                count += 1
                i += 1
                j -= 1
            # If the sum is less than 'k', move the 'i' pointer to the right to increase the sum
            elif nums[i] + nums[j] < k:
                i += 1
            # If the sum is greater than 'k', move the 'j' pointer to the left to decrease the sum
            else:
                j -= 1    

        return count