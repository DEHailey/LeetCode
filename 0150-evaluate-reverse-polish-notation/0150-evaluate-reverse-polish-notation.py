
class Solution(object):
    def evalRPN(self, tokens):
        stk = []
        for t in tokens:
            if t in '+-*/':
                b, a = stk.pop(), stk.pop()               
                
                if t == '+':
                    stk.append(a+b)
                elif t == '-':
                    stk.append(a-b)
                elif t == '*':
                    stk.append(a*b)
                else:
                    stk.append(int(float(a)/b))                      
                        
            else:
                stk.append(int(t))
                     
        return stk[0]
        