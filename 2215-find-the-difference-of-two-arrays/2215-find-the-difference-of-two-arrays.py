class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        r1 = []
        r2 = []
        
        for num in nums1:
            if num in nums2:
                continue
            else:
                if num not in r1:
                    r1.append(num)
            
        for num in nums2:
            if num in nums1:
                continue
            else:
                if num not in r2:
                    r2.append(num)
                
        return [r1, r2]