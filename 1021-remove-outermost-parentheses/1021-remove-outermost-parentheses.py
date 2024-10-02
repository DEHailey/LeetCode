class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        cnt = 0
        
        for i in s:
            if i == '(':
                if cnt > 0:
                    result.append(i)
                cnt += 1
            else:
                cnt -= 1
                if cnt > 0:
                    result.append(i)
                    
        return ''.join(result)