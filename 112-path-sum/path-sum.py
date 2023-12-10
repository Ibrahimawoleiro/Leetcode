# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Approach1
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum)
        
    def helper(self, root, targetSum):
        if root == None:
            return False
        if not root.left and not root.right:
            return targetSum - root.val == 0
        sub = targetSum - root.val
        
        l = False
        r = False

        if root.right:
            l = self.helper(root.right, sub)
        if root.left:
            r = self.helper(root.left,sub)
        
        return l or r
        