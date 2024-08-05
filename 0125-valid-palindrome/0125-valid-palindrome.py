class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        s = ''.join(char.lower() for char in s if char.isalnum())
        
        n = len(s)
        l, r = 0, n - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
            
        return True
        