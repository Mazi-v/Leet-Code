"""Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?"""
import queue

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a priority queue
        q = queue.PriorityQueue()
        
        # Initialize the result as the first element of the list
        res = nums[0]
        
        # Insert negated values into the priority queue
        for num in nums:
            q.put(-num)  # Negate the value to prioritize larger numbers
        
        # Retrieve the kth largest element
        while k != 0 and not q.empty():
            k -= 1
            res = -q.get()  # Negate again to get the original positive value
        
        return res