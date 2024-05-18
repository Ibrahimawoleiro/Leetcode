# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        n_count = 0
        q = queue.Queue()
        l = 0
        q.put(root)
        q.put(None)
        while not q.empty():
            curr = q.get()
            if curr:
                n_count += 1
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            else:
                if q.empty():
                    break
                else:
                    l += 1
                    q.put(None)
        return n_count

