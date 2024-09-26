class Solution(object):
    def wordPattern(self, pattern, s):
        map_key = {}
        map_value = {}
        
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
                      
        for k, v in zip(pattern, words):
            if k not in map_key:
                if v in map_value:
                    return False
                else:
                    map_key[k] = v
                    map_value[v] = k
            else:
                if map_key[k] != v:
                    return False
                
        return True
    
    