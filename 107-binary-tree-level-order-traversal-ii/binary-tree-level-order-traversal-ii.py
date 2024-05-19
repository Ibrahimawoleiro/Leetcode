# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = queue.Queue()
        stack = []
        c = []
        q.put(root)
        q.put(None)
        ans = []
        while not q.empty():
            curr = q.get()
            if curr:
                c.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            else:
                stack.append(c.copy())
                c = []
                if q.empty():
                    break
                else:
                    q.put(None)
        
        while stack:
            ans.append(stack.pop())

        return ans