class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list = []
        nums = sorted(nums)

        for i in range(len(nums)):
            
            x=nums[i] +1
            for j in range(i+1,len(nums)):       
                w = nums[j]
                if x == w:
                    list.append(x)
                    x=0
        
        return list
        
        