# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        dic = {}
        q = queue.Queue()
        q.put(root)
        visited = set()
        min_time = [0]
        b = None
        def helper(curr, time):
            if curr in visited:
                return 
            visited.add(curr)
            if time > min_time[0]:
                min_time[0] = time
            if curr.left:
                helper(curr.left, time + 1)

            if curr.right:
                helper(curr.right, time + 1)

            if curr in dic:
                helper(dic[curr], time + 1)


        while not q.empty():
            curr = q.get()
            if curr.val == start:
                b = curr
            if curr.left:
                q.put(curr.left)
                dic[curr.left] = curr
            if curr.right:
                q.put(curr.right)
                dic[curr.right] = curr

        helper(b, 0)
        return min_time[0]