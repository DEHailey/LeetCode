class Solution(object):
    def singleNumber(self, nums):
        for n in nums:
            if nums.count(n) == 1:
                return n
        
        