class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s = sorted(nums)
        res = []
        
        for i in range(0,len(nums)-1,2):
            res.extend([s[i+1], s[i]])
            
        return res
    