class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
 
        count = Counter(arr1)
        res = []  
        
        for i in arr2:
            res += [i]*count.pop(i)  
            
        return res + sorted(count.elements())
    
    