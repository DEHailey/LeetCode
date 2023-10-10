class Solution:
    def findSmallestSetOfVertices(self, n, edges):
        indegree = [0]*n
        for x, y in edges:
            indegree[y] += 1
            
        return [node for node in range(n) if indegree[node] == 0] 
        