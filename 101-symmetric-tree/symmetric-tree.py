# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.right and not root.left:
            return True
        if not root.right and root.left or root.right and not root.left:
            return False
        leftarr = []
        rightarr = []

        self.righthelper(root.right,rightarr,"root")
        self.lefthelper(root.left,leftarr,"root")
        return leftarr == rightarr
    def righthelper(self,root,arr,direction):
        
        if root.right:
            self.righthelper(root.right,arr,"r")

        arr.append(str(root.val)+direction)
        
        if root.left:
            self.righthelper(root.left,arr,"l")
        

    def lefthelper(self,root,arr,direction):
        if root.left:
            self.lefthelper(root.left,arr,"r")

        arr.append(str(root.val)+direction)
        

        if root.right:
            self.lefthelper(root.right,arr,"l")

