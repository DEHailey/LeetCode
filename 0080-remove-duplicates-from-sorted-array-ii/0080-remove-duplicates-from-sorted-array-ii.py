class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 1
        n = len(nums)
        count = 1
        
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                count += 1
            else:
                count = 1
                
            if count <= 2:
                nums[j] = nums[i]
                j += 1
                
        return j