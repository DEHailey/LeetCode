class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        pos = {}
        for i, c in enumerate(keyboard):
            pos[c] = i
            
        summ = 0
        for i in range(len(word)):
            if i == 0:
                summ += abs(0 - pos[word[i]])
            else:
                summ += abs(pos[word[i-1]] - pos[word[i]])
                
        return summ