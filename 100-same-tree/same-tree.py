# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # #Approach 1
        # arr1 = []
        # arr2 = []

        # def helper(root,array,direction):

        #     if not root:
        #         return 
                
        #     array.append(str(root.val) + direction)

        #     helper(root.left, array,'left') if root.left else array.append(None)
               
        #     helper(root.right, array,'right') if root.right else array.append(None)
                
        #     return array
        
        # return helper(p,arr1,'root') == helper(q,arr2,'root')

        #Approach 2
        if not p and not q:
            return True
        if not p and q or p and not q:
            return False
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)