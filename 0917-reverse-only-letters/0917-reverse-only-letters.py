class Solution(object):
    def reverseOnlyLetters(self, s):
        letters = [c for c in s if c.isalpha()]
        ans = []
        for i in s:
            if i.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(i)
                
        return ''.join(ans)