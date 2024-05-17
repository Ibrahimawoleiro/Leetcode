# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #Get the parent of each node into a map
        
        #When you are trying to get the  values away, You have three options
        #Go up
        #Go down left
        #Go down right
        ans = []
        visited = set()
        def helper(curr, d):
            if d > k or curr in visited:
                return 
            if d == k:
                ans.append(curr.val)
            visited.add(curr)
            if curr.left:
                helper(curr.left,d + 1)
            if curr.right:
                helper(curr.right, d + 1)
            if curr in dic:
                helper(dic[curr], d+ 1)
            

        dic = {}
        q = queue.Queue()
        q.put(root)
        
        start = target
        while not q.empty():
            curr = q.get()
            #Map children to their parents
            if curr.left:
                dic[curr.left] = curr
                q.put(curr.left)
            if curr.right:
                dic[curr.right] = curr
                q.put(curr.right)
        
        helper(target, 0)
        return ans