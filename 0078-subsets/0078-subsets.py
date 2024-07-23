class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [],[]
       
        def backtrack(i):
            if i == n:
                res.append(sol.copy())
                return
            
            # Don't pick num[i]
            backtrack(i+1)
            
            # Pick num[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
                       
        backtrack(0)
        return res
    
    
    # Time : O(2**n)
    # Space : O(n)