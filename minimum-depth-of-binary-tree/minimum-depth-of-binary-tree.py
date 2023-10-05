# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        left_depth = float('inf') if not root.left else self.minDepth(root.left)
        right_depth = float('inf') if not root.right else self.minDepth(root.right)
        
        return min(left_depth, right_depth) + 1