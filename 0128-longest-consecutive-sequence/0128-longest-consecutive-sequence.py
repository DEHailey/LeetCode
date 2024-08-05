class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        l = len(nums)
        ans = 1
        count = 1
        
        for i in range(l-1):
            if nums[i] == nums[i+1] - 1:
                count += 1
            else:
                count = 1
                
            ans = max(ans, count)
            
        return ans
        