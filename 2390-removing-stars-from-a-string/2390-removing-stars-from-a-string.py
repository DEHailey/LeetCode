class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in range(len(s)):
            if stack and s[i] == '*':
                stack.pop()
            else:
                stack.append(s[i])
        return ''.join(stack)
                
        