# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        p_left = p.left
        p_right = p.right
        q_left = q.left
        q_right = q.right
        return self.isSameTree(p_left, q_left) and self.isSameTree(p_right, q_right)
        