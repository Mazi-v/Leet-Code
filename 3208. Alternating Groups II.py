"""There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:
colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).
Return the number of alternating groups.
Note that since colors represents a circle, the first and the last tiles are considered to be next to each other."""
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors += colors[:k-1]  # Extend for circular check
        count = 1
        res = 0

        for i in range(1, len(colors)):
            if colors[i] != colors[i - 1]:
                count += 1
            else:
                if count >= k:
                    res += count - k + 1
                count = 1

        # Final group check
        if count >= k:
            res += count - k + 1

        return res