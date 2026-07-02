class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        line = "".join(chars)
        left = 0
        right = len(line) - 1
        while left < right: 
            if line[left] == line[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True