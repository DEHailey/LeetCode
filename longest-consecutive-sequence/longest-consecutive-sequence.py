class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        
        count = 1
        ans = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] or nums[i] == nums[i+1]-1:
                count += 1
            else:
                count = 1
            
            ans = max(ans, count)
            
        return ans