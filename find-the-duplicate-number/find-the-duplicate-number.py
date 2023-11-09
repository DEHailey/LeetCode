class Solution(object):
    def findDuplicate(self, nums):
        counts = defaultdict(lambda: 0)
        
        for num in nums:
            counts[num] += 1
            
        for num in counts:
            if counts[num] > 1:
                return num
            
        
            
        
        