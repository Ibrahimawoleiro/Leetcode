# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if root == None:
            return 

    
        if root.val == subRoot.val:
            result = self.helper(root,subRoot)
            if result:
                return result
        if root.left:
            l = self.isSubtree(root.left,subRoot)
            if l:
                return l
        if root.right:
            r = self.isSubtree(root.right,subRoot)
            if r:
                return r
        return False
        
    def helper(self,root,subRoot):

        if not root and not subRoot:
            return True

        if root and not subRoot or not root and subRoot:
            return False
        
        if root.val == subRoot.val:
            l = self.helper(root.left if root else None, subRoot.left if subRoot else None)
            r = self.helper(root.right if root else None, subRoot.right if subRoot else None)
            return l and r
        else:
            return False

