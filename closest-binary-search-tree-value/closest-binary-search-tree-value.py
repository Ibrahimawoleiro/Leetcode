# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        //Defined a list
        //Use an in order traversal on the tree
        //This gives an list that is sorted
        //Now we calculate the lowest distance to find the number closest to target
        """
        List = []
        self.helper(root,List)
        lowest_distance = 10 ** 5
        ans = 0
        for index in List:
            if abs(index - target) < lowest_distance:
                lowest_distance = abs(index - target)
                ans = index
            print(index, ans)
        return ans
        
    def helper(self,root,List=[]):
        if not root:
            return 
        
        if root.left:
            self.helper(root.left,List)
            
        List.append(root.val)
        
        if root.right:
            self.helper(root.right,List)
        
        
        
        