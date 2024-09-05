# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        row_tracker = 0
        q = Queue()
        ans = 0
        first = -1
        last = -1
        q.put((root, 0, 1))
        while not q.empty():
            node , row, p = q.get()
            if row > row_tracker:
                ans = max(ans, last - first + 1)
                row_tracker = row
                first = p
                last = p
            else:
                if first == -1:
                    first =  p
                last = p
            print(first, last)
            if node.left:
                q.put((node.left, row + 1, p * 2))
            if node.right:
                q.put((node.right, row + 1, p * 2 + 1))
        ans = max(ans, last - first + 1)
        return ans