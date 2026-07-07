class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mymap = {}
        longest = 0
        for i in range(len(s)):
            if s[i] in mymap and left <= mymap[s[i]]:
                left = mymap[s[i]]+1
            longest = max(longest, i-left+1)
            mymap[s[i]] = i
        return longest