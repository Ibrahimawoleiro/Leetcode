# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-float('inf')]
        self.helper(root, ans)
        return ans[0]
      
    
    def helper(self, node,ans):
        if not node:
            return 0

        l = self.helper(node.left,ans)
        r = self.helper(node.right,ans)

        curr = l + r + node.val
        curr_only = node.val
        l_and_curr = node.val + l
        r_and_curr = node.val + r
        
        result = max(curr, max(max(curr_only, l_and_curr), r_and_curr))
        ans[0] = max(result, ans[0])
        return max(max(l_and_curr, r_and_curr),curr_only)
        # heapq.heappush(heap, min(min(-curr, -node.val),-(node.val + max(l, r))))
        # return max(node.val + max(l, r), node.val)
