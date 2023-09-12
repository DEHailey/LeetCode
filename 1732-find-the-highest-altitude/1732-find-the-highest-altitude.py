class Solution(object):
    def largestAltitude(self, gain):
        prefix = [0]
        for i in range(len(gain)):
            prefix.append(gain[i]+ prefix[-1])
            
        return max(prefix)
        