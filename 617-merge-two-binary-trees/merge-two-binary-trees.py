# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(x,y):
            if not x and not y:
                return None
    
            if x and y:
                curr = TreeNode(x.val + y.val)
            elif x:
                y = TreeNode()
                curr = TreeNode(x.val + y.val)
            elif y:
                x = TreeNode()
                curr = TreeNode(x.val + y.val)

            if x.left or y.left:
                curr.left = helper(x.left if x.left else TreeNode(), y.left if y.left else TreeNode())
            
            if x.right or y.right:
                curr.right = helper(x.right if x.right else TreeNode(), y.right if y.right else TreeNode())
            return curr

        return helper(root1,root2)