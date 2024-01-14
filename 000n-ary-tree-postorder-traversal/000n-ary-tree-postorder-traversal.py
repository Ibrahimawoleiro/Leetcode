"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root,arr):
            if not root:
                return 
            
            for val in root.children:
                helper(val,arr)
                
            arr.append(root.val)

            
                
            return arr
        
        return helper(root,[])