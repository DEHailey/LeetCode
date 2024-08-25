class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        pos = {ch : i for i, ch in enumerate(t)}
        return sum([abs(i - pos[s[i]]) for i in range(len(s))])
        
        