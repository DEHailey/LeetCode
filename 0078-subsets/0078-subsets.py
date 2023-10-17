class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, idx):
            if idx > len(nums):
                return

            ans.append(curr[:])
            for j in range(idx, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j+1)
                curr.pop()
                
        ans = []
        backtrack([],0)
        return ans
