"""You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
"""

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_white = len(blocks)
        left = 0
        white_count = 0

        for right in range(len(blocks)):
            if blocks[right] == 'W':
                white_count += 1

            # Maintain window size of k
            if right - left + 1 > k:
                if blocks[left] == 'W':
                    white_count -= 1
                left += 1

            if right - left + 1 == k:
                min_white = min(min_white, white_count)

        return min_white

