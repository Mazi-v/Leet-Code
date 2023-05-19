#Given a string s, find the length of the longest substring without repeating characters.
#Sliding Window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i, j, result = 0, 0, 1  # Initialize two pointers and the result variable
        
        charSet = set()  # Create an empty set to store unique characters
        
        while len(s) > i and j < len(s):
            c = s[i]  # Current character at index i
            
            if s[j] not in charSet:
                charSet.add(s[j])  # Add the character at index j to the set
                j += 1  # Move the j pointer to the next position
            else:
                result = max(result, len(charSet))  # Update the result if necessary
                charSet = set()  # Reset the set
                i += 1  # Move the i pointer to the next position
                j = i  # Reset the j pointer to i
                
        return max(result, len(charSet))  # Return the maximum result
        