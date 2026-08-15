class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            mid = (right + left)//2
            sumv = 0
            for p in piles:
                sumv = sumv + (p + mid - 1)//mid
            if sumv <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left