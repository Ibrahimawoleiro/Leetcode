# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def re(node, overall_ans):
            if not node:
                return 0
            left = re(node.left, overall_ans)
            right = re(node.right, overall_ans)   
            if left + right > overall_ans[0]:
                overall_ans[0] = left+right
            return max(left, right) + 1    

        ans = [0]
        re(root, ans)
        return ans[0]