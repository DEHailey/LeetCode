class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        sorted_nums = sorted(nums)
        result = []
        
        for i in range(0, len(sorted_nums) - 1, 2):
            result.extend([sorted_nums[i + 1], sorted_nums[i]])
            
        return result