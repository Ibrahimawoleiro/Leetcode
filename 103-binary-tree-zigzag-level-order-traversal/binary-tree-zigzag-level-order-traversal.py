# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = []
        stack.append(root)
        count = 0
        while stack:
            level = []
            temp = []
            while stack:
                if count % 2 == 0:
                    curr = stack.pop()
                    level.append(curr.val)
                    if curr.left:
                        temp.append(curr.left)
                    if curr.right:
                        temp.append(curr.right)
                else:
                    curr = stack.pop()
                    level.append(curr.val)
                    if curr.right:
                        temp.append(curr.right)
                    if curr.left:
                        temp.append(curr.left)
            count+= 1
            ans.append(level)
            if temp:
                stack = temp

        return ans