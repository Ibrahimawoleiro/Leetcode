# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        max_num = root.val
        min_num = root.val
        
        maximum_difference = max_num-min_num
        
        return self.helper(root,max_num,min_num,maximum_difference)
        
    
    def helper(self,curr, maximum, minimum, maximum_difference):
        if not curr:
            return 0
        maximum = max(curr.val,maximum)
        
        minimum = min(curr.val, minimum)
        
        maximum_difference  = max(maximum_difference,maximum - minimum)
        print(maximum_difference)
        
        return max(maximum_difference,self.helper(curr.left,maximum,minimum,maximum_difference),self.helper(curr.right,maximum,minimum,maximum_difference))
    
    