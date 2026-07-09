class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        mymap = {}
        result = 0

        for i in range(len(s)):
            mymap[s[i]] = mymap.get(s[i],0) + 1
            maxf = max(maxf, mymap[s[i]])
            while((i-l+1)-maxf) > k:
                mymap[s[l]] -= 1
                l += 1
            result = max(result, i-l+1)
        return result