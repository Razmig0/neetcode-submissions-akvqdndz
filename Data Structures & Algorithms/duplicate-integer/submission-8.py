class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset =set()
        for i in range(1,len(nums)):
         n = nums[i]
         j = nums[i-1]
         if j == n:
           return True           
        return False
         