# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lower = float('-inf')
        upper = float('inf')
        def validate(node, lower, upper):
            if node is None:
                return True
            
            if node.val <= lower or node.val >= upper:
                return False
    
            return (validate(node.left, lower, node.val) and 
            validate(node.right, node.val, upper))
        return validate(root, lower, upper)
        