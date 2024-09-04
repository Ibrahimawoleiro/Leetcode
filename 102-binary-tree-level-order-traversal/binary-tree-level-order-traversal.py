# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = Queue()
        q.put(root)
        q.put(None)
        ans = []
        level = []
        while(not q.empty()):
            curr = q.get()
            if curr:
                level.append(curr.val)
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            else:
                print(q.qsize())
                ans.append(level)
                level = []
                if not q.empty():
                    q.put(None)
        return ans