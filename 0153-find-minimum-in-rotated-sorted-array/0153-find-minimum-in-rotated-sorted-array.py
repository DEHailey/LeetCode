class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums) -1
        l = 0
        r = n
        
        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        return nums[l]