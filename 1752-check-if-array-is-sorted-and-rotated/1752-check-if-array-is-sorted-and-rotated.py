class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count = 0
        if len(nums) < 3:
            return True
        
        for i in range (0,len(nums)):
            if nums[i] > nums[(i+1) % len(nums)]:
                count += 1
                
        if count == 1 or count == 0:
            return True
        else:
            return False