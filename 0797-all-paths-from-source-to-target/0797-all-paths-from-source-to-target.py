class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        target = len(graph)-1
        res = []
        
        def backtrack(curr, path):
            if curr == target:
                res.append(path[:])
                return
            
            for x in graph[curr]:
                path.append(x)
                backtrack(x,path)
                path.pop()
                
        path = [0]
        backtrack(0,path)
        
        return res
        