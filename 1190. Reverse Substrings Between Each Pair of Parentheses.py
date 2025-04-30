"""You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets."""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ")":
                stack.append(s[i])
                continue
            string = []
            while stack and stack[-1] != "(":
                string.append(stack.pop())
            if stack and stack[-1] == "(":
                stack.pop()
                stack.extend(string)
        return "".join(stack)
