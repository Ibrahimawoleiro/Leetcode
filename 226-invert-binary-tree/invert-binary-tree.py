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
        if not root:
            return root

        self.helper(root.left)
        self.helper(root.right)

        left = root.left
        right = root.right
        root.left = root.right
        root.right = left

        return root
        


    
