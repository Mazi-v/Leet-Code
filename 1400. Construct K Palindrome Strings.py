from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_frequency = Counter(s)
        odds = 0
        for count in char_frequency.values():
            if count%2==1: odds+=1
        return odds<=k and len(s)>=k