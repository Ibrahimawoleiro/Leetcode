# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)
    def helper(self,root):
        if root == None:
            return 
        
        r = root.right
        l = root.left

        root.right = l
        root.left = r

        if root.left:
            self.helper(root.left)
        if root.right:
            self.helper(root.right)

        return root
        


    
