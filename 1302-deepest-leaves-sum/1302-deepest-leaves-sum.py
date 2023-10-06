# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0

        queue = deque([root])
        while queue:
            level_sum = 0 
            level_size = len(queue) 

            for _ in range(level_size):
                current = queue.popleft()
                level_sum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if not queue:
                return level_sum

        return 0  