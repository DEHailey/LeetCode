class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        
        for c in s:
            d[c] = d.get(c, 0) + 1
            
        for c in t:
            d[c] = d.get(c, 0) - 1
            
        for k, v in d.items():
            if v < 0:
                return k