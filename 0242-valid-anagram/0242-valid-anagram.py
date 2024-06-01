class Solution(object):
    def isAnagram(self, s, t):
        s_count = [0] * 26
        t_count = [0] * 26
        
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1

        for i in range(len(t)):
            t_count[ord(t[i]) - ord('a')] += 1
        
        return s_count == t_count
        