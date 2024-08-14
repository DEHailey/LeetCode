class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_val = prices[0]
        max_pro = 0
        
        for price in prices[1:]:
            if price < min_val:
                min_val = price
            elif price > min_val:
                max_pro = max(max_pro, price - min_val)
                
        return max_pro
                