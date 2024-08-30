from collections import Counter

class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        wordMap = Counter()
        
        for word in words:
            curr = ''.join(sorted(set(word)))
            wordMap[curr] += 1
         
        pairs = 0
        for count in wordMap.values():
            pairs += count * (count-1) // 2
            
        return pairs
        
        