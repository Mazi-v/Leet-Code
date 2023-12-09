"""
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
"""
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Check if it's possible to form groups
        if len(hand) % groupSize != 0:
            return False
        
        # Count occurrences of each card value in the hand
        count = Counter(hand)
        heapify(hand)  # Convert hand to a min-heap
        
        # Check if it's possible to form groups
        while hand:
            curr = heappop(hand)  # Pop the minimum card value from the heap
            count[curr] -= 1  # Decrement the count of the current card
            
            # If the current card's count is still valid, try forming a group
            if count[curr] >= 0:
                # Check for consecutive cards to form a group
                for i in range(1, groupSize):
                    if curr + i in count and count[curr + i] > 0:
                        count[curr + i] -= 1  # Decrement the count of the next consecutive card
                    else:
                        return False  # If unable to form a group, return False
        
        return True  # All groups have been formed successfully