class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        
        for i in range(len(nums)):
            h[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
                
            if y in h and h[y] != i:
                return [i, h[y]]
            
        