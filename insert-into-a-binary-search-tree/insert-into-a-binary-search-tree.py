# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        if the root is empty, return a tree with value as the root node
        Else, look for the perfect location.
        How to look for the perfect location
        insert as child node
        """
        return self.helper(root,val)
        
    def helper(self,root,val):
        if not root:
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.helper(root.left,val)
        
        if root.val < val:
            root.right = self.helper(root.right,val)
        
        return root
        