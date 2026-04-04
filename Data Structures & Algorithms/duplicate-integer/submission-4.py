class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset =set()
        for n in nums:
            for j in nums:
             if n == j:
              return True
            
        return False
         