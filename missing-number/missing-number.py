class Solution(object):
    def missingNumber(self,nums):
        nums.sort()
        
        if nums[-1] != len(nums):
            return len(nums)
        
        elif nums[0] != 0:
            return 0
        
        
        for i in range(1,len(nums)):
            expected = nums[i-1]+1
            if nums[i] != expected:
                return expected
            
                
        