class Solution(object):
    def findMaxAverage(self, nums, k):
        left = 0
        right = k-1
        
        current_sum = sum(nums[:k])
        max_average = current_sum / float(k)
        
        while right < len(nums)-1:
            right += 1
            current_sum += nums[right] - nums[left]
            left += 1
            max_average = max(max_average, current_sum / float(k))
            
        return max_average
        