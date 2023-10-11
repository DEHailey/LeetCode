class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors = collections.defaultdict(list)
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        seen = [False]*n
        for node in restricted:
            seen[node] = True
            
        ans = 0
        queue = deque([0])
        seen[0] = True
        
        while queue:
            curr = queue.popleft()
            ans += 1
            
            for nextN in neighbors[curr]:
                if not seen[nextN]:
                    seen[nextN] = True
                    queue.append(nextN)
                    
        return ans