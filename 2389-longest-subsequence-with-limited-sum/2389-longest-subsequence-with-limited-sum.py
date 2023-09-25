class Solution(object):
    def answerQueries(self, nums, queries):
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            
        ans = []
        for q in queries:
            index = bisect.bisect_right(nums, q)
            ans.append(index)
            
        return ans