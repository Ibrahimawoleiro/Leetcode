# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def helper(x):
            if not x:
                return (0,0)

            l = (0,0)
            r = (0,0)
            if x.left:
                l = helper(x.left)
            if x.right:
                r = helper(x.right)
            print(l[0]+r[0], x.val)
            return (1 + max(l[0],r[0]), l[0]+r[0] if (l[0]+r[0] > r[1] and l[0]+r[0] > l[1]) else max(r[1], l[1]))
            
        return helper(root)[1]
            

