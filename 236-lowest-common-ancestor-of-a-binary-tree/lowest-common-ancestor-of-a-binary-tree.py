# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic = {}
        dic[p.val] = False
        dic[q.val] = False

        return self.helper(root, p,q,dic)[2][0]

    def helper(self,root, p, q, dic):
        if not root:
            return [False, False, [None, False]]
        l = self.helper(root.left, p, q, dic)

        r = self.helper(root.right, p, q, dic)
        if l[2][1]:
            return l
        if r[2][1]:
            return r
        if l[0] and r[1] or l[1] and r[0]:
            return [True,True,[root,True]]
        if p.val == root.val:
            if l[1]:
                return [True, True, [root, True]]
            elif r[1]:
                return [True, True, [root, True]]
        elif q.val == root.val:
            if l[0]:
                return [True, True, [root, True]]
            elif r[0]:
                return [True, True, [root, True]]
        
        return [ True if root.val == p.val or l[0] or r[0] else False, True if root.val == q.val or l[1] or r[1] else False, [None, False]]

