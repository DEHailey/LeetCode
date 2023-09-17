class Solution(object):
    def simplifyPath(self, path):
        stack = []
        
        for portion in path.split('/'):
            if portion == '..':
                if stack:
                    stack.pop()
            elif portion == '.' or not portion:
                continue
            else:
                stack.append(portion)
        
        return '/'+'/'.join(stack)
        