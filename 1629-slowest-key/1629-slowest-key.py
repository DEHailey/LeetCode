class Solution:
    def slowestKey(self, releaseTimes, keysPressed):
        k, t = keysPressed[0], releaseTimes[0]
        
        for i in range(1, len(keysPressed)):
            diff = releaseTimes[i] - releaseTimes[i-1] 
            if diff > t or (diff == t and keysPressed[i] > k):
                t = diff
                k = keysPressed[i]
        
        return k