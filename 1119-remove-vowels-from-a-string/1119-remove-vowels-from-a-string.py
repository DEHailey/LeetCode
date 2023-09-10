class Solution(object):
    def removeVowels(self, s):
        vowels = ['a','e','i','o','u']
        s_l = len(s)
        ans = []
        
        if not s:
            return None
        
        for i in range(s_l):
            if s[i] not in vowels:
                ans.append(s[i])
                
        return ''.join(ans)