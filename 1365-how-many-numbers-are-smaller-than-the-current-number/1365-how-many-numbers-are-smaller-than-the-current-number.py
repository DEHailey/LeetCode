class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        t = sorted(nums)
        h = {}
        res = []
        
        for i in range(len(t)):
            if not t[i] in h:
                h[t[i]] = i
                
        for i in range(len(nums)):
            res.append(h[nums[i]])
            
        return res
            
        
