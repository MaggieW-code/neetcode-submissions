class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = 0
        for price in prices:
            result = price - minp
            maxp = max(maxp, result)
            minp = min(minp, price)
        return maxp