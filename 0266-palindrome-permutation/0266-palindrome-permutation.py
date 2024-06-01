class Solution(object):
    def canPermutePalindrome(self, s):
        counter = collections.Counter(s)
        
        odd_chk = 0
        for count in counter.values():
            if count % 2:
                odd_chk +=1
            
            if odd_chk > 1:
                return False
            
        return True
            