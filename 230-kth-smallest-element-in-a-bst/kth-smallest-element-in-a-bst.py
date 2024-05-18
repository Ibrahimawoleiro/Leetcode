# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def helper(curr, check):
            if not curr:
                return [0, None]
            
            l = helper(curr.left,check)
            if l[0] == k:
                return l
            check[0] += 1

            if check[0] == k:
                check[1] = curr.val
                return check
            
            return helper(curr.right, check)
        
        return helper(root, [0,0])[1]