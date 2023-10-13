# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node,parent):
            if not node:
                return
            
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)
        queue = deque([target])
        seen = {target}
        dist = 0
        
        while queue and dist < k:
            curr_l = len(queue)
            for _ in range(curr_l):
                node = queue.popleft()
                for neigh in [node.left, node.right, node.parent]:
                    if neigh and neigh not in seen:
                        seen.add(neigh)
                        queue.append(neigh)
                        
            dist += 1
            
        return [node.val for node in queue]