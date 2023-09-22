#Given an integer array nums, return the length of the longest strictly increasing subsequence.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Create an array to store the length of the longest increasing subsequence ending at each index.
        result = [1] * len(nums)
        
        # Start iterating through the array from the second-to-last element to the first element.
        for i in range(len(nums) - 2, -1, -1):
            # Iterate through all elements to the right of the current element.
            for j in range(i, len(nums)):
                # If the current element (nums[i]) is less than the element to the right (nums[j]),
                # update the length of the longest increasing subsequence ending at index 'i'.
                if nums[i] < nums[j]:
                    result[i] = max(result[i], result[j] + 1)
        
        # The maximum value in the 'result' array represents the length of the longest increasing subsequence.
        return max(result)
