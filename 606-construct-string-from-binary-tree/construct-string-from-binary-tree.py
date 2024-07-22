# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = []
        ans.append(f'{root.val}')
        def helper(curr):
            if not curr:
                return ans
            if curr != root:
                ans.append('(')
                ans.append(f'{curr.val}')
            if curr.left and curr.right:
                helper(curr.left)
                helper(curr.right)
            elif curr.left:
                helper(curr.left)
            elif curr.right:
                ans.append('()')
                helper(curr.right)
            else:
                if curr != root:
                    ans.append(')')
                return ans
            if curr != root:
                ans.append(')')
            return ans

        helper(root)

        return ''.join(ans)