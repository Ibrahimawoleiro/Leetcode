# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #Approach 1
        ans = []
        count = 0
        level_sum = 0
        queue = deque()
        queue.append(root)
        queue.append(None)
        while(queue):
            current = queue.popleft()
            if current:
                level_sum += current.val
                count+=1
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            else:
                ans.append(level_sum/count if count else 1)
                level_sum = count = 0
                if len(queue) > 0:
                    queue.append(None)

        return ans


