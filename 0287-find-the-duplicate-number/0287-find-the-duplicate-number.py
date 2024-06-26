class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # step1. prove we have a cycle
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow is fast:
                break
        
        # step2. find where the cycle is (by resetting both to 1x speed)
        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow