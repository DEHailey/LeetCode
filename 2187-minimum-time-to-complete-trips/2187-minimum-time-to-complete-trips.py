class Solution(object):
    def minimumTime(self, time, totalTrips):
        left, right = 1, max(time)*totalTrips
        
        def timeEnough(given_time):
            actual_trips = 0
            for t in time:
                actual_trips += given_time // t
            return actual_trips >= totalTrips
        
        while left < right:
            mid = (left+right) // 2
            if timeEnough(mid):
                right = mid
            else:
                left  = mid + 1
        
        return left
        
        