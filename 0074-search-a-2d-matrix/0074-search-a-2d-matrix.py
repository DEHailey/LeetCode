class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        t = m * n
        l, r = 0, t-1
        
        while l <= r:
            mid = (l + r)//2
            i = mid //n
            j = mid % n
            
            mid_num = matrix[i][j]
            
            if target == mid_num:
                return True
            elif target > mid_num:
                l = mid + 1
            else:
                r = mid - 1
                
        return False
            
