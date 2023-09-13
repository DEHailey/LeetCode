class Solution(object):
    def minSubArrayLen(self, target, nums):
        start, end = 0,0
        n = len(nums)
        min_length = float('inf')
        curr_sum = 0
        
        while end < n:
            curr_sum += nums[end]
        
            while curr_sum >= target:
                min_length = min(min_length, end-start+1)
                curr_sum -= nums[start]
                start += 1
            end += 1
            
        if min_length != float('inf'):
            return min_length
        else:
            return 0            