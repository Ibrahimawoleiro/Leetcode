# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        //First of all, put the tree in a list using inorder traversal
        //This will lead to a sorted list
        //Then check marker, 
            //if the marker is < than or equal to 0.5
                //Loop through the list starting from the front and return the last number that is                          lower than target
            //if the marker is > than 0.5
                //loop through the list starting from the back and return the last number that is                           greater than target
        
        //
        """
        List = []
        self.helper(root,List)
        print(List)
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
        
        
        
        