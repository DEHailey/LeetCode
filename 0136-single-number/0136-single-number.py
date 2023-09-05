class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        for n in nums:
            if nums.count(n) == 1:
                return n
        
        