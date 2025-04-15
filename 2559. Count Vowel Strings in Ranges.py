from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        res = [0] * (len(words) + 1)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Precompute prefix sums of words that start and end with a vowel
        for i in range(1, len(res)):
            res[i] = res[i-1]
            if words[i-1][0] in vowels and words[i-1][-1] in vowels:
                res[i] += 1

        # Answer queries using the prefix sums
        ans = []
        for s, e in queries:
            ans.append(res[e+1] - res[s])
        
        return ans
