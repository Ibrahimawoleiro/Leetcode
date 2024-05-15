# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]
    def helper(self,root):
        if not root:
            return [0,True]
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left[1] == False or right[1] == False:
            return [0,False]
        if abs(left[0] - right[0]) <= 1:
            return [1 + max(left[0], right[0]), True]
        return [0, False]
        