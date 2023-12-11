# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root1,root2)

    def helper(self, r1, r2):
        if not r1 and not r2:
            return 

        root = TreeNode(0, None, None)
        if r1 and not r2:
            root.val = r1.val
        if not r1 and r2:
            root.val = r2.val

        if r1 and r2:
            root.val = r1.val + r2.val

        root.left = self.helper(r1.left if r1 else None, r2.left if r2 else None)
        root.right = self.helper(r1.right if r1 else None, r2.right if r2 else None)

        return root
