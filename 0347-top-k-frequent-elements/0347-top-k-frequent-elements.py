class Solution(object):
    def topKFrequent(self, nums, k):
        count = dict()
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = count.get(n,0) +1 
            
        items = sorted(count.items(), key = lambda x:x[1] ,reverse = True)
        return [item[0] for item in items[:k]]
        