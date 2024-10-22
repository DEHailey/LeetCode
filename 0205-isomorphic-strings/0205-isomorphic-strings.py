class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dic = {}
        t_dic = {}
        
        for c1, c2 in zip(s, t):
            if s_dic.get(c1) != t_dic.get(c2):
                return False
            s_dic[c1] = t_dic[c2] = c2
        return True
            
        