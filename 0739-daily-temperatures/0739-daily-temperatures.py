class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        temp = temperatures
        n = len(temp)
        stk = []
        ans = [0]*n
        
        for i, t in enumerate(temp):
            while stk and stk[-1][0] < t:
                stk_t, stk_i = stk.pop()
                ans[stk_i] =  i - stk_i
            stk.append((t,i))
                
        return ans
            
            