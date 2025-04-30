"""There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.

The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.

Return the maximum number of customers that can be satisfied throughout the day."""
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        total_satisfied = 0

        # Base satisfaction from already non-grumpy minutes
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        # Sliding window to find the best interval 
        extra_satisfied = 0
        max_extra = 0
        for i in range(len(customers)):
            if grumpy[i] == 1:
                extra_satisfied += customers[i]
            if i >= minutes and grumpy[i - minutes] == 1:
                extra_satisfied -= customers[i - minutes]
            max_extra = max(max_extra, extra_satisfied)

        return total_satisfied + max_extra
