# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def re(node, ans):
            if not node:
                return
            re(node.left, ans)
            re(node.right, ans)
            ans.append(node.val)
            return ans
        return re(root, ans)