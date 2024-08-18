class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        
        join = list(zip(heights,names))
        join_sort = sorted(join, key=lambda x:x[0], reverse=True)
        
        res = [name for height, name in join_sort]
        
        return res