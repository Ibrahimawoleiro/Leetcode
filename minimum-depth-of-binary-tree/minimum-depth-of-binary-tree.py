# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        """
        Cases: No children, 1 child, 2 chilren
        
        No children:
        When a node has no chilren, return 1 + min(left node count, right node count)
        
        1 child: 
        When a node has 1 child, only return the information from that child
        """
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
    