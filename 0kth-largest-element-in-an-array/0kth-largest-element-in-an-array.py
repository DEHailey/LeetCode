import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        cnt = 0
        while cnt < k:
            largest = heapq.heappop(heap)
            cnt += 1
            
        return -largest
        