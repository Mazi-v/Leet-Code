"""We have a wooden plank of the length n units. Some ants are walking on the plank, each ant moves with a speed of 1 unit per second. Some of the ants move to the left, the other move to the right.

When two ants moving in two different directions meet at some point, they change their directions and continue moving again. Assume changing directions does not take any additional time.

When an ant reaches one end of the plank at a time t, it falls out of the plank immediately.

Given an integer n and two integer arrays left and right, the positions of the ants moving to the left and the right, return the moment when the last ant(s) fall out of the plank.
"""

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # When ants collide, it is the same as if there were no collision in terms of calculating the time.
        # Calculate the time when the last ant moving to the right falls off the plank
        # by finding the distance from the rightmost ant's position to the right end of the plank.
        r = (n) - min(right) if right else 0

        # Calculate the time when the last ant moving to the left falls off the plank
        # by finding the distance from the leftmost ant's position to the left end of the plank.
        l = max(left) if left else 0

        # Return the maximum of the two times, which represents when the last ant falls off the plank.
     
        return max(l, r)