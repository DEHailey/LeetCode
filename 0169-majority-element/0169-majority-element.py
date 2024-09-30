class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        
        for n in nums:
            h[n] = h.get(n, 0) + 1
            
        lst = [k for k, v in h.items() if v > len(nums) // 2]
        ans = lst[0]
        
        return ans