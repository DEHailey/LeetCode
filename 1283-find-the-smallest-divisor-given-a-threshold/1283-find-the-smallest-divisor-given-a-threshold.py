class Solution:
    def smallestDivisor(self, nums, threshold):
        def find_division_sum(divisor):
            result = 0
            for num in nums:
                result += ceil((1.0 * num) / divisor)
            return result
        
        ans = -1
        low = 1
        high = max(nums)
        
        while low <= high:
            mid = (low + high) // 2
            result = find_division_sum(mid)
            
            if result <= threshold:
                ans = mid
                high = mid - 1
           
            else:
                low = mid + 1
        
        return ans