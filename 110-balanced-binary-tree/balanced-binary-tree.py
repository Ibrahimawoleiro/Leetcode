# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def re(node):
            if not node:
                return [0, True]

            left = re(node.left)
            right = re(node.right)

            if not left[1] or not right[1]:
                return [0, False]
            return [max(left[0] , right[0]) + 1, abs(left[0] - right[0]) <= 1]

        return re(root)[1]
        