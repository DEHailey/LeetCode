class Solution(object):
    def sortedSquares(self, nums):
        ans = []
        for n in nums:
            sq = n*n
            ans.append(sq)
            
        return sorted(ans)
            
        