# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_child = root.left
        right_child = root.right

        depth = 1 + max(self.maxDepth(left_child),self.maxDepth(right_child))
        return depth
        