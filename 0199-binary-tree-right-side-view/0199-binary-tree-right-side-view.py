from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = deque()
        queue.append(root)
        
        while queue:
            rightSide = None
            n = len(queue)
            
            for i in range(n):
                node = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if rightSide:
                ans.append(rightSide.val)
                
        return ans