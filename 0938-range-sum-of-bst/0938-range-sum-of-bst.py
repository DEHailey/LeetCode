# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low, high):
        stack = ([root])
        ans = 0
        
        while stack:
            root = stack.pop()
            
            if low <= root.val <= high:
                ans += root.val
            
            if root.left and low < root.val:
                stack.append(root.left)
            if root.right and root.val < high:
                stack.append(root.right)
                
        return ans
            
            
        
        