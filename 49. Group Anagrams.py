"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result ={}
        for s in strs:
            sortedS= ''.join(sorted(s))
            if sortedS in result:
                result[sortedS].append(s)
            else:
                result[sortedS]=[s]   
        return result.values()      


