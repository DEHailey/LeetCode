class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        seen = set()
        
        for num in collections.Counter(arr).values():
            if num in seen:
                return False
            else:
                seen.add(num)
        
        return True