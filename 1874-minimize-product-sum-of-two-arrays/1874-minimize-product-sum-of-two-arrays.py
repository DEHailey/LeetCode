class Solution(object):
    def minProductSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        return sum([x*y for x, y in zip(sorted(nums1), sorted(nums2, reverse=True))])