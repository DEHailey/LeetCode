class Solution:
    def findMaxAverage(self, nums, k):
        best = now = sum(nums[:k])
        for i in range(k,len(nums)):
            now += nums[i] - nums[i-k]
            if now>best:
                best = now
        return best / float(k)
        