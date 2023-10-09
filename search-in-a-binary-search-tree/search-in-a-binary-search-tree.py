# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        ans = self.helper(root,val)
        return ans
    def helper(self,root,val):
        if not root:
            return None
        
        if(root.val == val):
            return root
        
        left = self.helper(root.left,val)
        if(left != None and left.val == val):
            return left
        
        right = self.helper(root.right,val)
        if(right != None and right.val == val):
            return right