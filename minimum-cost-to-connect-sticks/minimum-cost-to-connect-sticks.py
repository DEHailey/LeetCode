import heapq
class Solution(object):
    def connectSticks(self, sticks):
        heapq.heapify(sticks)
        
        ans = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            new_stick = first + second
            ans += new_stick
            heapq.heappush(sticks, new_stick)
            
        return ans
        