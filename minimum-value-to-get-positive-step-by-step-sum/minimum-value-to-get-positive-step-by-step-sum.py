class Solution(object):
    def minStartValue(self, nums):
        start_val = 1
        
        while True:
            curr_sum = start_val
            is_valid = True
            
            for num in nums:
                curr_sum += num
                
                if curr_sum < 1:
                    is_valid = False
                    break
                    
            if is_valid:
                return start_val
            else:
                start_val += 1
            