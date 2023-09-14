class Solution(object):
    def checkIfPangram(self, sentence):
        s = set()
        
        for i in range(len(sentence)):
            s.add(sentence[i])
            
            if len(s) == 26:
                return True
        
        return False