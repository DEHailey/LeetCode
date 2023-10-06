# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        
        result = []  
        queue = [root]

        level = 0 
        while queue:
            level_values = [] 
            next_level = [] 

            for node in queue:
                level_values.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level % 2 == 1:
                level_values = level_values[::-1]

            result.append(level_values)
            queue = next_level
            level += 1

        return result

