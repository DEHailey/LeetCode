class Solution:
    def slowestKey(self, r, k):
        times = {r[0]: [k[0]]}
        
        for i in range(1 , len(r)):
            t = r[i] - r[i - 1]
            if(t in times):
                times[t].append(k[i])
            else:
                times[t] = [k[i]]
        
        keys = times[max(times.keys())]
        
        return max(keys)