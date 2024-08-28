class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        arr = [0] * 201
        count = 0
        
        for num in nums: 
            arr[num] += 1
        
        for num in nums: 
            count += arr[num + k]

        return count