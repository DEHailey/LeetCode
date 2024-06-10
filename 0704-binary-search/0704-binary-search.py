class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i , n in enumerate(nums):
            if n == target:
                return i
            elif target not in nums:
                return -1
            
        