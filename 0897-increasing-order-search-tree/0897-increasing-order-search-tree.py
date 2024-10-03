# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.curr.right = node
                self.curr = node
                inorder(node.right)
                
        ans = self.curr = TreeNode(None)
        inorder(root)
        
        return ans.right
    