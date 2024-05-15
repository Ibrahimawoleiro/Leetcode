# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import heapq
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        heap = []
        self.helper(root, heap)
        return heapq.heappop(heap) * -1
    
    def helper(self, node, heap):
        if not node:
            return 0

        l = self.helper(node.left,heap)
        r = self.helper(node.right, heap)
        curr = l + r + node.val
        curr_only = node.val
        heapq.heappush(heap, min(min(-curr, -node.val),-(node.val + max(l, r))))
        return max(node.val + max(l, r), node.val)
