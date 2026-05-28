class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            if nums[i] in n:
                n[nums[i]].append(i)
            else:
                n[nums[i]] = [i]
        
        for key, value in n.items():
            f = target - key
            if f == key:
                if len(value) > 1:
                    return [value[0], value[1]]
            elif f in n:
                return [value[0], n[f][0]]

