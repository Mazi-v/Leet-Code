"""You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell."""

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions_sorted = sorted(potions)  # Sorting the potions list
        result = [0] * len(spells)  # Initializing the result list with zeros

        # Looping through each spell
        for i in range(len(spells)):
            start = 0  # Start index of potions
            end = len(potions_sorted) - 1  # End index of potions
            count = 0  # Variable to store the count of successful pairs for the current spell

            # Binary search to find the count of successful pairs for the current spell
            while start <= end:
                mid = start + ((end - start) // 2)  # Calculating the middle index

                # Checking if the product of strengths satisfies the success condition
                if potions_sorted[mid] * spells[i] >= success:
                    count = len(potions_sorted) - mid  # Updating the count of successful pairs
                    end = mid - 1  # Continue searching on the left side for more potential successes
                else:
                    start = mid + 1  # Move to the right side of the potions list

            # Assigning the count to the result for the current spell
            result[i] = count

        return result