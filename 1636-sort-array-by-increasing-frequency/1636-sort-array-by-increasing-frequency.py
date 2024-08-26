class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
            
        return sorted(nums, key = lambda x: (counts[x], -x))