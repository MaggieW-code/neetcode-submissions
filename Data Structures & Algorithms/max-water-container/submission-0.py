class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        while left < right:
            temp = (right-left)*(min(heights[left],heights[right]))
            if temp > water:
                water = temp
            elif heights[left] < heights[right]: 
                left = left + 1
            else:
                right = right - 1
        return water
