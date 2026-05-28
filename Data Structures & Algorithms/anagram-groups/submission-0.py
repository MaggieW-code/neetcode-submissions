class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = {}
        for i in strs:
            key = ""
            x = sorted(i)
            for j in range(len(x)):
                key += x[j]
            if key in n:
                n[key].append(i)
            else:
                n[key] = [i]
            
        ans = []
        for key, value in n.items():
            ans.append(value)
        return ans