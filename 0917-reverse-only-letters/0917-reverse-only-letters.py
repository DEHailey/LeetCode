class Solution(object):
    def reverseOnlyLetters(self, s):
        letters = [c for c in s if c.isalpha()]
        
        ans = []
        for c in s:
            if c.isalpha():
                ans.append(letters.pop())
                
            else:
                ans.append(c)
                
        return "".join(ans)
        
        