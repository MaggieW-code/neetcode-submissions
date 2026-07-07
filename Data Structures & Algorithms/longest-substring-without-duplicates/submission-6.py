class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ex = {}
        longest = 0

        for i in range(len(s)):
            if s[i] in ex and ex[s[i]] >= left:
                left = ex[s[i]] + 1

            longest = max(longest, i - left + 1)
            ex[s[i]] = i

        return longest