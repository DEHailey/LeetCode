class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        ans = []
        
        for spell in spells:
            left, right = 0, len(potions)-1
            count = 0
            
            while left <= right:
                mid = (left+right)//2
                if spell * potions[mid] >= success:
                    count += right - mid + 1
                    right = mid - 1
                else:
                    left = mid + 1
                    
            ans.append(count)
            
        return ans