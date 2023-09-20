class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        next_greater = {}
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        result = []
        for num in nums1:
            result.append(next_greater.get(num, -1)) 
            
        return result