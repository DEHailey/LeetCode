class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_val = max(nums)
        
        for i in range(len(nums)):
            if nums[i] == max_val:
                return i
            else:
                continue
            
        