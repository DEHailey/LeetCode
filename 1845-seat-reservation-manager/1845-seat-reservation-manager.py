class SeatManager(object):

    def __init__(self, n):
        self.heap = list(range(1,n+1))
        

    def reserve(self):
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber):
        return heapq.heappush(self.heap, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)