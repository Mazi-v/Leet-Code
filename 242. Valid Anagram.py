"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once."""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency =[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)) :
            indexS = ord(s[i])-97
            frequency[indexS]+=1
            indexT = ord(t[i])-97
            frequency[indexT]-=1
        return max(frequency)==min(frequency)==0

