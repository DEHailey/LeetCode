class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(map(min, zip(s,s[::-1])))