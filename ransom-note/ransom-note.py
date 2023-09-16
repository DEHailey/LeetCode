class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ran_counts = collections.Counter(ransomNote)
        mag_counts = collections.Counter(magazine)
        
        for char, count in ran_counts.items():
            if count > mag_counts[char]:
                return False
        return True
        

            
            
        