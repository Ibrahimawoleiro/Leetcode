# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def re(n, m):
            if not n and not m:
                return True
            if not n and m or n and not m or n.val != m.val:
                return False
            return re(n.left, m.left) and re(n.right, m.right)

        return re(p,q)