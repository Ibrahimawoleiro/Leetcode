# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import queue
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = [None]
        q = queue.Queue()
        q.put(root)
        q.put(None)
        ans = []
        while not q.empty():

            curr = q.get()

            if curr:
                l[0] = curr
                if curr.left:
                    q.put(curr.left)
                if curr.right:
                    q.put(curr.right)
            else:
                ans.append(l[0].val)
                if q.empty():
                    break
                else:
                    q.put(None)
        
        return ans

            

    

        