class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        seen = [False]*n
        for node in restricted:
            seen[node] = True
        
        ans = 0
        def dfs(currN):
            nonlocal ans
            ans += 1
            seen[currN] = True
            
            for nextN in graph[currN]:
                if not seen[nextN]:
                    dfs(nextN)
                    
        dfs(0)
        
        return ans