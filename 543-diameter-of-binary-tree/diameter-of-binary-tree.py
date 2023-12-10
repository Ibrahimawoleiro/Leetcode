# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
        
    def helper(self,root):
        if not root.left and not root.right:
            return [0,0]
        
        l = None
        r = None

        if root.left:
            l = self.helper(root.left)
        
        if root.right:
            r = self.helper(root.right)

        if l and r:
            l[0] = l[0] + 1
            r[0] = r[0] + 1

            curr = []
            if l[0] > r[0]:
                curr.append(l[0])
            else:
                curr.append(r[0])

            if l[1] > l[0] + r[0]:
                curr.append(l[1])
            elif r[1] > l[0] + r[0]:
                curr.append(r[1])
            else:
                curr.append(l[0] + r[0])
            
            return curr
        elif root.right:
            r[0]+=1
            if r[0] > r[1]:
                r[1] = r[0]
            return r
        else:
            l[0]+=1
            if l[0] > l[1]:
                l[1] = l[0]
            return l
        
        
        
        