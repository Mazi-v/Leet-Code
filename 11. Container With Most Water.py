"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize two pointers, s and e, at the beginning and end of the height array.
        s, e = 0, len(height) - 1
        # Initialize a variable to store the maximum area.
        result = 0
        # Continue looping as long as s is less than e.
        while s < e:
            # Calculate the area between the current pointers (s and e).
            current_area = (e - s) * min(height[e], height[s])
            # Update the maximum area if the current area is larger.
            result = max(current_area, result)
            
            # Move the pointers based on the height of the walls.
            if height[e] <= height[s]:
                e -= 1  # If the right wall is shorter or equal, move the right pointer left.
            else:
                s += 1  # If the left wall is shorter, move the left pointer right.
        
        return result
