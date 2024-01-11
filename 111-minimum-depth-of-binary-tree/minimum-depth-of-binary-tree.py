# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def helper(x):
            if not x:
                return 0
            if not x.left and not x.right:
                return 1

            if x.left and x.right:
                return 1 + min(helper(x.left), helper(x.right))
            
            if x.right:
                return 1 + helper(x.right)
            
            if x.left:
                return 1 + helper(x.left)

        return helper(root)
            

        