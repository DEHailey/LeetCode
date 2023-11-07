class Solution(object):
    def getWinner(self, arr, k):
        n = len(arr)
        winner = arr[0]
        win_count = 0
        
        for i in range(n-1):
            if arr[i+1] > winner:
                winner = arr[i+1]
                win_count = 1
                
            else:
                win_count += 1
                
            if win_count == k:
                return winner
            
        return winner
        