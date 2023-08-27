class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            nums_set.add(num)
        return False