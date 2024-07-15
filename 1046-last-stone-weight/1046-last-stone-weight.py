import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            
            add = largest - next_largest
            if largest != next_largest:
                heapq.heappush(stones, add)
                
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0
        
            
        
        