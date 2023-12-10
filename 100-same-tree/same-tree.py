# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #     #Approach1
    #def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     arr1 = []
    #     arr2 = []

    #     self.helper(p, arr1,'beginning',0)
    #     self.helper(q, arr2, 'beginning',0)

    #     return arr1 == arr2

    # def helper(self,root, arr, direction, count):
    #     if root == None:
    #         return 
    #     arr.append(str(root.val)+direction+str(count))
    #     if root.left:
    #         self.helper(root.left, arr, 'l', count+1)
    #     if root.right:
    #         self.helper(root.right,arr, 'r',count+1)

    #Approach2
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p,q)

    def helper(self,root1, root2):
        if not root1 and not root2:
            return True
        if not root1 and root2 or root1 and not root2:
            return False
        if root1.val != root2.val:
            return False

        r =self.helper(root1.right, root2.right)
        l =self.helper(root1.left, root2.left)

        return r and l 
        