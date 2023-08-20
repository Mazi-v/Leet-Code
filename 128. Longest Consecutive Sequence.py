"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time."""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 :
            return 0
        num_set = set(nums)
        
        longest_sequence_length = 1  
        
        for num in nums:
            current_sequence_length = 1  
            # Check if the previous number is not present, indicating the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                # Increment current_num while the next number is in the set
                while current_num + 1 in num_set:
                    current_num += 1
                    current_sequence_length += 1
                
                # Update the longest sequence length
                longest_sequence_length = max(longest_sequence_length, current_sequence_length)
        
        return longest_sequence_length