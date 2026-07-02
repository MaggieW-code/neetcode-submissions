class Solution:
    def isPalindrome(self, s: str) -> bool:
        line = ""
        for i in range (0,len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                line = line + s[i].lower()
        left = 0
        right = len(line) - 1
        while left < right: 
            if line[left] == line[right]:
                left = left + 1
                right = right - 1
            else:
                return False
        return True