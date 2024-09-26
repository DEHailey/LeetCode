class Solution(object):
    def wordPattern(self, pattern, s):
        map_key = {}
        map_value = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
                      
        for k, v in zip(pattern, words):
            if k in map_key and map_key[k] != v:
                return False
            if v in map_value and map_value[v] != k:
                return False
            
            map_key[k] = v
            map_value[v] = k
        
        return True
    
    