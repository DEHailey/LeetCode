# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        self.buildGraph(root, None, graph)
        
        queue = [(target,0)]
        visited = set([target])
        res = []
        
        while queue:
            node, dist = queue.pop(0)
            
            if dist == k:
                res.append(node.val)
                
            if dist > k:
                break
                
            for neigh in graph[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    queue.append((neigh,dist+1))
                                    
        return res
    
    def buildGraph(self, node, parent, graph):
        if not node:
            return
        
        if node not in graph:
            graph[node] = []
            
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
            
        self.buildGraph(node.left, node, graph)
        self.buildGraph(node.right, node, graph)
                    