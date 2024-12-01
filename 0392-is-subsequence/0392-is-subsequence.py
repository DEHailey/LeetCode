class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        '''
        res = ''
        
        if len(s) == 0 and len(t) != 0:
            return True
        
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    res += t[i]
            i += 1
            j += 1
            
        return s == res
        '''
        j = 0  # s의 인덱스를 추적
        
        # t를 순회하며 s의 문자를 찾음
        for char in t:
            if j < len(s) and s[j] == char:
                j += 1  # s의 다음 문자로 이동
            
        # s의 모든 문자를 순서대로 찾았는지 확인
        return j == len(s)
                    