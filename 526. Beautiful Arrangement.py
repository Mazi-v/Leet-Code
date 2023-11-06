"""Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a beautiful arrangement if for every i (1 <= i <= n), either of the following is true:

perm[i] is divisible by i.
i is divisible by perm[i].
Given an integer n, return the number of the beautiful arrangements that you can construct."""
class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0  # Initialize a counter to keep track of beautiful arrangements count

        def findBeautifulArrangements(position):
            if len(arrangement) == n:
                # If the arrangement is complete, increment the count and return
                self.count += 1
                return

            for num in range(1, n + 1):
                if not used[num]:
                    arrangement.append(num)
                    used[num] = True

                    # Check if the current number satisfies the beautiful arrangement condition
                    if arrangement[-1] % len(arrangement) == 0 or len(arrangement) % arrangement[-1] == 0:
                        findBeautifulArrangements(position + 1)  # Recursively explore next positions

                    arrangement.pop()  # Backtrack
                    used[num] = False  # Mark the number as unused

        used = [False] * (n + 1)  # Initialize an array to keep track of used numbers
        arrangement = []  # Initialize the arrangement
        findBeautifulArrangements(1)  # Start with the first position
        return self.count  # Return the count of beautiful arrangements
   
     

