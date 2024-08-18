class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = list(zip(names, heights))
        people_sorted = sorted(people, key = lambda x:x[1], reverse=True) 
        
        res = [name for name, heights in people_sorted]
        
        return res