"""Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0, and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game."""
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # Initialize consecutive wins required to determine the winner
        consecutive_wins = k
        
        # Iterate through the elements of the array
        for i in range(len(arr)):
            j = i + 1
            # Play rounds of the game by comparing arr[i] with arr[j]
            while j < len(arr) and arr[i] > arr[j]:
                j += 1    
                consecutive_wins -= 1
            # If an integer wins k consecutive rounds, return it as the winner
            if consecutive_wins <= 0:
                return arr[i]
            # Reset consecutive wins for the next round
            consecutive_wins = k - 1
            i = j
        # If no winner is found in first round, return the maximum value in the array,
        # which will definitely win the next round as the larger integer remains at position 0.
        return max(arr)