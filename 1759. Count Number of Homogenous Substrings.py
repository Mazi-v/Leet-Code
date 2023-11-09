"""Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 10^9 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string."""

class Solution:
    def countHomogenous(self, s: str) -> int:
        total_homogenous_count = 0  
        current_homogenous_count = 0 
        previous_char = s[0] 
        mod = 10**9 + 7 

        for i in range(len(s)):
            if previous_char == s[i]:
                current_homogenous_count += 1
            else:
                # Calculate and add the count of homogenous substrings for the previous character
                total_homogenous_count += ((current_homogenous_count * (current_homogenous_count + 1)) // 2)
                current_homogenous_count = 1  # Reset count for the current character
                previous_char = s[i]

        # Add the count of homogenous substrings for the last character
        total_homogenous_count += ((current_homogenous_count * (current_homogenous_count + 1)) // 2)

        return total_homogenous_count % mod