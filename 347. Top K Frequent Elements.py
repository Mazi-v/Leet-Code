"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        keys = []
        values=[]
        result=[]
        for num in nums:
            if num in keys :
                i = keys.index(num)
                values[i]+=1
            else:
                values.append(1)
                keys.append(num)
        while k>0:
            num = max(values)
            i = values.index(num)
            result.append(keys[i])
            values.remove(num)
            keys.remove(keys[i])
            k-=1
        return result    

