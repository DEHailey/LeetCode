class Solution(object):
    def maxNumberOfBalloons(self, text):
        return min(text.count('b'), text.count('a'), text.count('l')//2,text.count('o')//2,text.count('n'))
        
        