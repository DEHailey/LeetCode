import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        
        for i in range(k):
            res = heapq.heappop(heap)
            
        return  - res