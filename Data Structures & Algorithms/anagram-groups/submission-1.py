class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = {}
        for i in strs:
            x = sorted(i)
            key = ""
            for j in range(len(x)):
                key += x[j]
            if key in n:
                n[key].append(i)
            else:
                n[key] = [i]
        
        list1 = []
        for key, value in n.items():
            list1.append(value)
        return list1