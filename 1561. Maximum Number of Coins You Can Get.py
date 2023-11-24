"""There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have."""
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)  # Sort the piles in ascending order
        left = 0  # Index for the last person (bob)
        right = len(piles) - 2  # Index for the second person (you)
        total_coins = 0  # Total coins collected
        
        while left < right:
            # The second person (you) pick the second largest pile
            total_coins += piles[right]
            # Move two steps to the left for the second person
            right -= 2
            # Move one step to the right for the last person
            left += 1
        
        return total_coins