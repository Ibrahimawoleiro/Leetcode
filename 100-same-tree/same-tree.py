# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #Approach1
        arr1 = []
        arr2 = []

        self.helper(p, arr1,'beginning',0)
        self.helper(q, arr2, 'beginning',0)

        return arr1 == arr2

    def helper(self,root, arr, direction, count):
        if root == None:
            return 
        arr.append(str(root.val)+direction+str(count))
        if root.left:
            self.helper(root.left, arr, 'l', count+1)
        if root.right:
            self.helper(root.right,arr, 'r',count+1)
        