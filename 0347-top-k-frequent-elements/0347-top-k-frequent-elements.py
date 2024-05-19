class Solution(object):
    def topKFrequent(self, nums, k):
        counts = collections.Counter(nums)
        heap = []
        
        for key, val in counts.items():
            heapq.heappush(heap, (val,key))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [pair[1] for pair in heap]
        
        
            
        