# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.right and root.left:
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            return min(1+left,1+right)
        elif root.right:
            right = self.minDepth(root.right)
            return 1 + right
        elif root.left:
            left = self.minDepth(root.left)
            return 1 + left
        else:
            return 1
    