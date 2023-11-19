"""Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:

Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
Reduce nums[i] to nextLargest.
Return the number of operations to make all elements in nums equal."""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)  # Sort the input array
        operations_count = 0  # Initialize count of operations
        length = len(sorted_nums)  # Length of the array

        # Loop through the array backwards (from end to start)
        for i in range(length - 1, 0, -1):
            # If the current number is greater than the previous number,
            # increment count by the difference in indices (length - i)
            if sorted_nums[i] > sorted_nums[i - 1]:
                operations_count += (length - i)

        return operations_count