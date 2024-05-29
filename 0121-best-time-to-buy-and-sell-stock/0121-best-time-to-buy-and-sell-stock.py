class Solution(object):
    def maxProfit(self, prices):
        min_val = prices[0]
        max_profit = 0
        
        for price in prices[1:]:
            if price < min_val:
                min_val = price
            elif price - min_val > max_profit:
                max_profit = price - min_val
                
        return max_profit
        