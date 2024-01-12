# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #Approach1
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def helper(root,sum_so_far):
            if not root:
                return False
            sum_so_far += root.val
            if not root.left and not root.right and sum_so_far == targetSum:
                return True
            
            if root.left:
               l =  helper(root.left,sum_so_far)
               print('lk')
               if l:
                   return l
            if root.right:
                r = helper(root.right,sum_so_far)
                print('lnk')
                if r:
                    return r

            return False

        return helper(root,0)
        