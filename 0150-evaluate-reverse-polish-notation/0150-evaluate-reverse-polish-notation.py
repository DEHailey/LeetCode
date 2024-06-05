from math import ceil, floor
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
                    if a * b < 0 and a % b != 0:
                        stk.append(a // b + 1)
                    else:
                        stk.append(a // b)                       
                        
            else:
                stk.append(int(t))
                     
        return stk[0]
        