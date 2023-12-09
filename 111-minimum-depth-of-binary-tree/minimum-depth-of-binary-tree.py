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
        return self.helper(root)

    def helper(self, current):
        if current.left == None and current.right == None:
            return 1
        if current.left:
            l = 1 + self.helper(current.left)
        if current.right:
            r = 1 + self.helper(current.right)
        if current.left and current.right:
            return min(l,r)
        elif current.left:
            return l
        else:
            return r 