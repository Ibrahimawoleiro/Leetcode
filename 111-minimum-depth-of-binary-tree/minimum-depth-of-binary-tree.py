# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
    #     #Approach1-DFS/recursion
    #     if root == None:
    #         return 0
    #     return self.helper(root)

    # def helper(self, current):
    #     if current.left == None and current.right == None:
    #         return 1
    #     if current.left:
    #         l = 1 + self.helper(current.left)
    #     if current.right:
    #         r = 1 + self.helper(current.right)
    #     if current.left and current.right:
    #         return min(l,r)
    #     elif current.left:
    #         return l
    #     else:
    #         return r 

        #Approach2-BFS
        if root == None:
            return 0
        count = 0
        queue = deque()
        queue.append(root)
        queue.append(TreeNode(None,None,None))
        while(queue):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            if current.left == None and current.right == None and current.val!= None:
                return count + 1
            if current.val == None:
                count+=1
                if(len(queue) > 0):
                    queue.append(current)
        
        return count

        