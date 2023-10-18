class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(curr_s,left_c,right_c):
            if len(curr_s) == n * 2:
                ans.append(''.join(curr_s))
                return
            
            if left_c < n:
                curr_s.append("(")
                backtrack(curr_s,left_c+1,right_c)
                curr_s.pop()
                
            if right_c < left_c:
                curr_s.append(")")
                backtrack(curr_s,left_c,right_c+1)
                curr_s.pop()
                
        backtrack([],0,0)
        return ans
                