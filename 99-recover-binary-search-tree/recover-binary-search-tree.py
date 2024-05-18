# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        def helper(curr):
            if not curr:
                return
            helper(curr.left)
            ans.append(curr.val)
            helper(curr.right)
        helper(root)
        ans.sort()

        def h(curr):
            if not curr:
                return
            h(curr.right)
            curr.val = ans.pop()
            h(curr.left)
        h(root)

            
        