class Solution(object):
    def smallestDivisor(self, nums, threshold):
        def sumSolution(divisor):
            result = 0
            for num in nums:
                result += ceil((1.0*num)/divisor)
            return result
        
        ans = -1
        low = 1
        hight = max(nums)
        
        while low <= hight:
            mid = (low + hight) // 2
            result = sumSolution(mid)
            
            if result <= threshold:
                hight = mid - 1
                
            else:
                low = mid + 1
        
        return low
            
        
        