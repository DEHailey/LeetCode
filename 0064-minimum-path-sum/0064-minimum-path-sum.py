class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for row in range(m):
            for col in range(n):
                if row + col == 0:
                    continue
                    
                ans = float('inf')
                if row > 0:
                    ans = min(ans, dp[row-1][col])
                if col > 0:
                    ans = min(ans, dp[row][col-1])
                    
                dp[row][col]=grid[row][col]+ans
                
        return dp[m-1][n-1]
                
        