class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            ans[key].append(s)
            
        return ans.values()
            
            
        