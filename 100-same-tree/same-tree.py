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
        elif not p and q or not q and p:
            return False
        left_Tree = []
        right_Tree = []

        self.helper(p,"root",left_Tree)
        self.helper(q,"root",right_Tree)

        return left_Tree == right_Tree

    def helper(self,root,direction,arr):

        if root.left:
            self.helper(root.left,"l",arr)
        
        arr.append(str(root.val)+direction)

        if root.right:
            self.helper(root.right,"r",arr)