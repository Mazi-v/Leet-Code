"""Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together."""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2+1):
            if len(s)%(i+1)==0 and (i+1)!=len(s):
                arr= s.split(s[0:i+1])
                array_string = ''.join(map(str, arr))
                if array_string=="":

                    return True        
        return False                

