"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order."""
from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def combination(temp, num):
            if len(temp) == k:
                res.append(temp.copy())
                return
            for i in range(num, n + 1):
                temp.append(i)
                combination(temp, i + 1)
                temp.pop()

        combination([], 1)
        return res
