class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []
        
        for c in candies:
            if c + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)
        
        return res