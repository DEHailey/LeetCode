class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """    
        h = {}
    
        for c in s:
            if c in h:
                h[c] += 1
            else:
                h[c] = 1
                
        for i, c in enumerate(s):
            if h[c] == 1:
                return i
        
        return -1