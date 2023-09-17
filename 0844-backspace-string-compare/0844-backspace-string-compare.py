class Solution(object):
    def backspaceCompare(self, s, t):
        stack_s =[]
        for char in s:
            if stack_s and char == '#':
                stack_s.pop()
            elif char != '#':
                stack_s.append(char) 
        
        stack_t =[]
        for char in t:
            if stack_t and char == '#':
                stack_t.pop()
            elif char != '#':
                stack_t.append(char)
                
        return stack_s == stack_t