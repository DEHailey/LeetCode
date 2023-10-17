class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        letters = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def backtrack(idx, path):
            if len(path) == len(digits):
                ans.append(''.join(path))
                return 
            
            for letter in letters[digits[idx]]:
                path.append(letter)
                backtrack(idx+1, path)
                path.pop()
                
        ans = []
        backtrack(0,[])
        return ans