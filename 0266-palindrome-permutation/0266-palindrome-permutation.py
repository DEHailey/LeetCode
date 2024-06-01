class Solution(object):
    def canPermutePalindrome(self, s):
        return sum(v%2 for v in Counter(s).values()) < 2
            