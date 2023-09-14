class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        cost=0
        j=0
        ans=0
        
        for i in range(len(s)):
            cost += abs(ord(s[i])-ord(t[i]))
            
            while cost > maxCost:
                cost -= abs(ord(s[j])-ord(t[j]))
                j+=1
                
            ans = max(ans, i-j+1)
            
            
        return ans