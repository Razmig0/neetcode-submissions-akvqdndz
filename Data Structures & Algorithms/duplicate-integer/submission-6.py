class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset =set()
        for i in len(nums):
         n = nums[i]
         j = nums[i+1]
         if n == j:
           return True           
        return False
         