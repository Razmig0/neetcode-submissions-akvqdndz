class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t = target
        for i in range(len(nums)):
         for j in range(1, len(nums)):
            n = nums[i]
            g = nums[j]
            if n + g == t:
                return [i,j]
        return False

