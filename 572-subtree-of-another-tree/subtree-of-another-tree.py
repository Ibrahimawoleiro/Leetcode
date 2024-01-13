# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return
        
        if root.val == subRoot.val:
            if self.helper(root.left,subRoot.left) and self.helper(root.right,subRoot.right):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

    def helper(self,root,subRoot):
        if not subRoot and not root:
            return True
        if not subRoot and root:
            return False
        if subRoot and not root:
            return False
        
        if subRoot.val != root.val:
            return False
        
        return self.helper(root.left, subRoot.left) and self.helper(root.right, subRoot.right)

        
        