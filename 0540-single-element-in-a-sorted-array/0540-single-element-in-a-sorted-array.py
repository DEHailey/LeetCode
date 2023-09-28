class Solution(object):
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = (left + right) // 2
            if mid % 2==0:
                if nums[mid]==nums[mid+1]:
                    left = mid + 2
                else:
                    right = mid
            if mid % 2 ==1:
                if nums[mid]==nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid
                    
        return nums[left]
            