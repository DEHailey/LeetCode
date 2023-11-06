class Solution(object):
    def checkIfPangram(self, sentence):
        n = len(sentence)
        lst = [0]*26
        
        for i in range(n):
            lst[ord(sentence[i]) - ord('a')] = 1
            
        return True if sum(lst) == 26 else False
        