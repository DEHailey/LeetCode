class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dist = [c for c in arr if arr.count(c) == 1]
        
        return "" if k > len(dist) else dist[k-1]