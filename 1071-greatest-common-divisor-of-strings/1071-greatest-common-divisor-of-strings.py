class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        def is_valid_length(k):
            if len1 % k != 0 or len2 % k != 0:
                return False
            
            base = str1[:k]
            if str1 != base * (len1 // k):
                return False
            if str2 != base * (len2 // k):
                return False
            
            return True

        for length in range(min(len1, len2), 0, -1):
            if is_valid_length(length):
                return str1[:length]

        return ""