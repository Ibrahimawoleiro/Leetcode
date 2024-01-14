"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def helper(root,arr):
            if not root:
                return 

            arr.append(root.val)

            for val in root.children:
                helper(val,arr)
                
            return arr
        
        return helper(root,[])
            
        
        
        
        
        