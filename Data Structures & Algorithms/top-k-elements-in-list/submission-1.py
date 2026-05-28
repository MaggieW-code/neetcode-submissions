class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numlist = sorted(nums)
        n = {}
        for i in numlist:
            if i in n:
                n[i]+=1
            else:
                n[i]=1
        
        sortedn = sorted(n, key=n.get, reverse=True)
        return(sortedn[0:k])