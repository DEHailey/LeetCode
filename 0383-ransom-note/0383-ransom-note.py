class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        rsn_count = collections.Counter(ransomNote)
        mag_count = collections.Counter(magazine)

        for char, count in rsn_count.items():
            if count > mag_count[char]:
                return False
        return True

            
            
        