# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        
        if not root.left:
            return right_depth + 1
        elif not root.right:
            return left_depth + 1
        else:
            return min(left_depth, right_depth) + 1
            
        