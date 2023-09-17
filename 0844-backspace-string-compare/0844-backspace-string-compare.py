class Solution(object):
    def backspaceCompare(self, s, t):
        def check(s):
            stack = []
            for char in s:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return check(s) == check(t)
            
        