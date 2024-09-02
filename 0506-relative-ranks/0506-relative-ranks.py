class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(score, reverse=True)
        
        ranks = {}
        
        for i, num in enumerate(sorted_score):
            if i == 0:
                ranks[num] = "Gold Medal"
            elif i == 1:
                ranks[num] = "Silver Medal"
            elif i == 2:
                ranks[num] = "Bronze Medal"
            else:
                ranks[num] = str(i + 1)

        return [ranks[num] for num in score]