class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        for n in nums:
            val = n*n
            ans.append(val)
            
        ans.sort()
        
        return ans
        
        