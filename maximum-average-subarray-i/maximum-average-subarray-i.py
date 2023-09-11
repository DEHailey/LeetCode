class Solution:
    def findMaxAverage(self, nums, k):
        left, right = 0, k - 1 
        current_sum = sum(nums[:k])  
        max_average = current_sum / float(k)
        
        while right < len(nums) - 1:
            right += 1
            current_sum += nums[right] - nums[left]  
            left += 1
            max_average = max(max_average, current_sum / float(k))
            
        return max_average
            
            
            