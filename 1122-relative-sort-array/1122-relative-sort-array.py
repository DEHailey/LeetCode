class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        # make a counter (manually count)
        count = {}
        
        for element in arr1:
            if element in count:
                count[element] += 1
            else:
                count[element] = 1
        
        # put the elements in 'res' depends on how many times in a counter
        res = []
        for i in arr2:
            res += [i] * count[i]
            del count[i]
        
        # put the elements in 'remain'
        remain = []
        for key in count:
            remain += [key] * count[key]
            
        # merge 'res' & 'remain'
        return res + sorted(remain)