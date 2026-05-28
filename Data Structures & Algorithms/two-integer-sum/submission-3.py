class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = {}
        for i in range(len(nums)):
            if nums[i] in l:
                l[nums[i]].append(i)
            else:
                l[nums[i]] = [i]
        
        for key, value in l.items():
            v = target - key
            if v == key:
                if len(value) > 1:
                    return [value[0], value[1]]
            elif v in l:
                return [value[0], l[v][0]]

