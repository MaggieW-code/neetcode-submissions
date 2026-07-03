class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        sumv = 0
        while left != len(prices)-1:
            for i in range(left, len(prices)-1):
                dif = prices[right] - prices[left]
                sumv = max(dif, sumv)
                if right!= len(prices)-1:
                    right = right + 1
            left = left + 1
            right = left + 1
        return sumv
        