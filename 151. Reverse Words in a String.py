class Solution(object):
    """
        Given an input string s, reverse the order of the words.
        A word is defined as a sequence of non-space characters.
        The words in s will be separated by at least one space.
        Return a string of the words in reverse order concatenated by a single space.
        Do not include any extra spaces(leading or trailing spaces or multiple spaces).
    """
    def reverseWords(self, s):
            
        words = []
        temp = ""
        
        for c in s:
            if c == " ":
                # If the character is a space, it indicates the end of a word
                # Append the temporary word to the list of words
                words.append(temp)
                # Reset the temporary word
                temp = ""
            else:
                # If the character is not a space, add it to the temporary word
                temp += c
        
        # Append the last word
        words.append(temp)
        res = ""
        # Iterate over the words in reverse order
        for word in words[::-1]:
            # If the word is not an empty string (to handle multiple spaces)
            if word != "":
                # Concatenate the word with a space and add it to the final result
                res += (word + " ")
        
        # Remove the trailing space and return the reversed words
        return res[:-1]