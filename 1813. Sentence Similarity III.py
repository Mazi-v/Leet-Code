"""You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces."""

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        count = 0 

        for i in range(min(len(s1), len(s2))):
            if s1[i] == s2[i]:
                count += 1
                continue
            break

        j = len(s2) - 1
        for k in range(len(s1) - 1, -1, -1):
            if j < 0 or s1[k] != s2[j]:
                break
            j -= 1
            count += 1

        return count >= len(s1) or count >= len(s2)
