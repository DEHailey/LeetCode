class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1]*n
        l = 1
        r = 1
        for i in range(n):
            res[i]*=l
            l*=nums[i]
            
        for i in range(n-1,-1,-1):
            res[i]*=r
            r*=nums[i]
            
        return res