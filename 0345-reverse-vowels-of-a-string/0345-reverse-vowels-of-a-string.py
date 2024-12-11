class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for c in s:
            if c in 'aeiouAEIOU':
                vowels.append(c)
        
        res = []
        for c in s:
            if c in 'aeiouAEIOU':
                res.append(vowels.pop())
            else:
                res.append(c)
            
        return ''.join(res)