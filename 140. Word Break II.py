"""Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        # Check if a word exists in the dictionary
        def isValidWord(word):
            return word in wordDict

        # Recursive backtracking to build valid word sequences
        def backtracking(s, temp):
            if len(s) == 0:
                res.append(" ".join(temp))
                return
            for i in range(len(s)):
                prefix = s[:i + 1]
                if isValidWord(prefix):
                    backtracking(s[i + 1:], temp + [prefix])

        backtracking(s, [])
        return res
