class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {}
        count = 0
        
        for num in nums:
            d[num] = d.get(num, 0) + 1
            count += d.get(num - k, 0)
            count += d.get(num + k, 0)
                
        return count