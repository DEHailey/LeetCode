class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')':'(', '}':'{',']':'['}
        
        for c in s:
            if c in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[c] != top_element:
                    return False
            
            else:
                stack.append(c)
                
        return not stack
        
        
        
        