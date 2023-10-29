# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        return self.helper(0,root,targetSum)
    def helper(self,sum_to_parent, current, targetSum):

        if(not current.left and not current.right):
            if sum_to_parent + current.val == targetSum:
                return True
            
         
        sum_to_current = current.val + sum_to_parent

        if current.left:
            checkerL=self.helper(sum_to_current,current.left,targetSum)
            if checkerL == True:
                return checkerL
        if current.right:
            checkerR = self.helper(sum_to_current,current.right,targetSum)
            if checkerR == True:
                return checkerR