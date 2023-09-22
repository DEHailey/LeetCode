class Solution(object):
    def findClosestElements(self, arr, k, x):
        heap = []
        
        for num in arr:
            distance = abs(x-num)
            heapq.heappush(heap, (-distance, -num))
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return sorted([-pair[1] for pair in heap])
        