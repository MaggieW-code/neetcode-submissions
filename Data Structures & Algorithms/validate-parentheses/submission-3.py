class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        if len(s) <= 1:
            return False
        for i in range(len(s)):
            if s[i] in pair: 
                if len(stack) > 0 and pair[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if not stack:
            return True 
        else:
            return False 