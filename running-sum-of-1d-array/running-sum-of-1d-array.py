class Solution(object):
    def runningSum(self, nums):
        prefix = [nums[0]]
        
        for i in range(1,len(nums)):
            prefix.append(nums[i]+prefix[-1])
            
        return prefix
            