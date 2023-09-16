import collections

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        stones_counts = collections.Counter(stones)  
        cnt = 0
        for i in range(len(jewels)):
            if jewels[i] in stones_counts:
                cnt += stones_counts[jewels[i]]
        return cnt