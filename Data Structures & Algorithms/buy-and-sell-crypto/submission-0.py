class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = (len(prices)+1)*[0]
        for i in range(len(prices)-1, -1, -1):
            maxp[i] = max(prices[i], maxp[i+1])

        result = 0
        for j in range(0,len(prices)):
            result = max(result,(maxp[j+1]-prices[j]))
        return result