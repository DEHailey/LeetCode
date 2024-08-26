class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dist = [i for i in arr if arr.count(i) == 1]
	    
        return "" if k > len(dist) else dist[k - 1]