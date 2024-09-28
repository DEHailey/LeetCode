class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarysearch(arr, target):
            lo, hi = 0, len(arr) - 1 
            
            while lo <= hi:
                mid = (lo + hi) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return -1

        i = binarysearch(nums, target)
        if i == -1:
            return [-1, -1]

        j = i
        while j > 0 and nums[j - 1] == target:
            j -= 1

        k = i
        while k < len(nums) - 1 and nums[k + 1] == target:
            k += 1

        return [j, k]
        
            