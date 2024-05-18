# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        qu = queue.Queue()
        qu.put(root)
        while not qu.empty():
            curr = qu.get()
            if curr.val < q.val and curr.val > p.val or curr.val < p.val and curr.val > q.val:
                return curr
            if curr.val == p.val or curr.val == q.val:
                return curr
            if curr.left:
                qu.put(curr.left)
            if curr.right:
                qu.put(curr.right)
        
