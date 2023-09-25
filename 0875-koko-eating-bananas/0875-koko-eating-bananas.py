import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        def check(k):
            hours = 0
            for bananas in piles:
                hours += (bananas + k - 1) // k  
            
            return hours <= h
        
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left