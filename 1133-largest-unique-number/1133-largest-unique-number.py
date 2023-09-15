class Solution(object):
    def largestUniqueNumber(self, nums):
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        
        nums.sort()
        for n in nums[::-1]:
            if counts[n] == 1:
                return n
                
        return -1        
            
            
        