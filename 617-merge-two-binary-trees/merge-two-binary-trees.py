# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # #Approach1
        # def helper(x,y):
        #     if not x and not y:
        #         return None
    
        #     if x and y:
        #         curr = TreeNode(x.val + y.val)
        #     elif x:
        #         y = TreeNode()
        #         curr = TreeNode(x.val + y.val)
        #     elif y:
        #         x = TreeNode()
        #         curr = TreeNode(x.val + y.val)

        #     if x.left or y.left:
        #         curr.left = helper(x.left if x.left else TreeNode(), y.left if y.left else TreeNode())
            
        #     if x.right or y.right:
        #         curr.right = helper(x.right if x.right else TreeNode(), y.right if y.right else TreeNode())
        #     return curr

        # return helper(root1,root2)

        if not root1 and not root2:
            return None
        
        value1 = root1.val if root1 else 0

        value2 = root2.val if root2 else 0

        root3 = TreeNode(value1 + value2)

        root3.left = self.mergeTrees(root1.left if root1 else None,root2.left if root2 else None)
        root3.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return root3