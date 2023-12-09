# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # #Approach1
        # q1 = deque()
        # arr = []
        # q1.append(root)
        # while q1:
        #     count = 0
        #     total = 0
        #     q2 = deque()
        #     while(q1):
        #         current = q1.popleft()
        #         if current.left:
        #             q2.append(current.left)
        #         if current.right:
        #             q2.append(current.right)
        #         total+=current.val
        #         count+=1
        #     arr.append(total / count)
        #     q1 = q2
        # return arr

        #Approach2
        q1 = deque()
        count = total = 0
        arr = []
        q1.append(root)
        q1.append( TreeNode(None, None,None))
        while(q1):
            current = q1.popleft()
            if current.val != None:
                total+= current.val
                count+=1
                if current.left:
                    q1.append(current.left)
                if current.right:
                    q1.append(current.right)
            elif current.val == None:
                arr.append(total/count)
                total = 0
                count = 0
                if len(q1) != 0:
                    q1.append(current)
        
        return arr
