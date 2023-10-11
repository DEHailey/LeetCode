class Solution:
    def countComponents(self, n, edges):
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
                    
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
                   
        seen = set()
        ans = 0
        
        for i in range(n):
            if i not in seen:
                ans += 1
                seen.add(i)
                dfs(i)
                
        return ans