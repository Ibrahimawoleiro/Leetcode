# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root,-2**32,2**32)
    
    def helper(self,root,left_bound, right_bound):
        if not root:
            return True
        
        left = self.helper(root.left,left_bound,root.val)
        if not left:
            return False

        right = self.helper(root.right,root.val,right_bound)
        if not right:
            return False

        if root.val <= left_bound or root.val >= right_bound:
            return False

        return True