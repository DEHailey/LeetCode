class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors = collections.defaultdict(list)
        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
            
        seen = [False]*n
        for node in restricted:
            seen[node] = True
            
        def dfs(curr):
            self.ans += 1
            seen[curr] = True
            
            for nextN in neighbors[curr]:
                if not seen[nextN]:
                    dfs(nextN)
                    
        self.ans = 0
        dfs(0)
        return self.ans