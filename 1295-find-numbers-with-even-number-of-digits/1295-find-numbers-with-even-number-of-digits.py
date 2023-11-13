class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            num_digit = 0
            while num > 0:
                num //= 10
                num_digit += 1
            
            if num_digit % 2 == 0:
                count += 1
        return count
                
        