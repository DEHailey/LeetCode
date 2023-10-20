class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
       
        back_two = nums[0]
        back_one = max(nums[0],nums[1])
        
        for i in range(2,n):
            back_one, back_two = max(back_one, back_two + nums[i]), back_one
            
        return back_one