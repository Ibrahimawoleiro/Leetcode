# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # #Approach 1
        # def helper(x):
        #     if not x:
        #         return 0
        #     if not x.left and not x.right:
        #         return 1

        #     if x.left and x.right:
        #         return 1 + min(helper(x.left), helper(x.right))
            
        #     if x.right:
        #         return 1 + helper(x.right)
            
        #     if x.left:
        #         return 1 + helper(x.left)

        # return helper(root)

        #Approach 2
        if not root:
            return 0
        queue = deque()
        level = 0

        queue.append(root)
        queue.append(None)

        while(queue):
            current = queue.popleft()
            if current:
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                if not current.left and not current.right:
                    return level + 1
            else:
                level+=1
                if queue:
                    queue.append(None)

        return level


            

        