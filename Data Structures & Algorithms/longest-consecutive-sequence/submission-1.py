class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0
        longest = 0
        for num in numset:
            if num-1 not in numset:
                count = 1
                current = num
                while num+1 in numset:
                    count += 1
                    num += 1
                longest = max(count, longest)
        return longest