class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m*n-1
        
        while left <= right:
            mid = (left+right) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            
            if num == target:
                return True
            elif num > target:
                right = mid -1
            elif num < target:
                left = mid + 1
        
        return False
                
        