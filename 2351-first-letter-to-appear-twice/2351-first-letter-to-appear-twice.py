class Solution(object):
    def repeatedCharacter(self, s):
        for i in range(len(s)):
            c = s[i]
            for j in range(i):
                if s[j] == c:
                    return c

        return ""
        