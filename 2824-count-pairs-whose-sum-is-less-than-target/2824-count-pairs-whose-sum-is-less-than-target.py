class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        count = 0
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            if nums[lo] + nums[hi] < target:
                count += (hi - lo)
                lo += 1
            else:
                hi -= 1
        
        return count