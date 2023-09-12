class Solution:
    def getAverages(self, nums, k):
        if k == 0:
            return nums
        n = len(nums)
        averages = [-1]*n
        
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
            
        for i in range(k, n-k):
            leftbound, rightbound = i-k, i+k
            subArraySum = prefix[rightbound+1]-prefix[leftbound]
            average = subArraySum // (k * 2 + 1)
            averages[i] = average
            
        return averages
            
            