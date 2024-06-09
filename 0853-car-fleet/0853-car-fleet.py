class Solution(object):
    def carFleet(self, target, position, speed):
        times = [float(target-p)/s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        
        for t in times[::-1]:
            if t > cur:
                res += 1
                cur = t
                
        return res
            
        
        
        

        
        
