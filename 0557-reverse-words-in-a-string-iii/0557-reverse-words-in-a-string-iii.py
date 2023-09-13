class Solution(object):
    def reverseWords(self, s):
        n = s.split()
        ans = []
        
        for i in n:
            ans.append(i[::-1])
           
        return ' '.join(ans)
        
        
        