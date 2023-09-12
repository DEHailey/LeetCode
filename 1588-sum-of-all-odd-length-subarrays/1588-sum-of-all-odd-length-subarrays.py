class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        result = 0
    
        for i in range(n):
            for j in range(i, n, 2):
                result += sum(arr[i:j+1])
    
        return result

            
        
        
        
        