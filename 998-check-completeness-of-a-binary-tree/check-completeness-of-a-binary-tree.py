
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        q = []
        
        q.append(root)

        last_seen = False

        while q:

            curr = q.pop(0)

            if curr:
                print(curr.val)
                if last_seen:
                    return False
                if curr.right and curr.left:
                    q.append(curr.left)
                    q.append(curr.right)
                elif curr.left:
                    q.append(curr.left)
                    q.append(None)
                elif curr.right:
                    q.append(None)
                    q.append(curr.right)
                else:
                    q.append(None)
                    q.append(None)
            else:
                last_seen = True

        print(last_seen)
        return True
