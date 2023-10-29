# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        return self.helper(p,q)

    def helper(self,left_tree,right_tree):
        if not left_tree and not right_tree:
            return True
        if not left_tree and right_tree:
            return False
        if not right_tree and left_tree:
            return False

        if right_tree.val != left_tree.val:
            return False

        return self.helper(left_tree.left,right_tree.left) and self.helper(left_tree.right,right_tree.right)