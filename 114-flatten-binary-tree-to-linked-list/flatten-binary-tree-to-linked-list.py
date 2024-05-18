# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        def helper(curr):
            if not curr:
                return None
            temp = curr.right
            curr.right = helper(curr.left)
            curr.left = None
            h = curr
            while(h.right):
                h = h.right
            h.right = helper(temp)
            return curr

        helper(root)

        