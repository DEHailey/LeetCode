class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] *26
        max_count = 0
        
        for task in tasks:
            freq[ord(task) -ord('A')] += 1
            max_count = max(max_count, freq[ord(task) -ord('A')])
            
        time = (max_count - 1) * (n+1)
        for f in freq:
            if f == max_count:
                time += 1
                
        return max(len(tasks), time)