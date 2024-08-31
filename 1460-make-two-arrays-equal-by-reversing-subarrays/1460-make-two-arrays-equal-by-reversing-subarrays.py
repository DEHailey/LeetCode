from collections import Counter
class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        
        if sorted(target) == sorted(arr):
            return True
        else: 
            return False