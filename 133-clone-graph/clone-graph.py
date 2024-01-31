"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def helper(current,copy):
            if not current:
                return 
            print(current.val)
            if current.val in seen:
                return seen[current.val]
            copy = Node(current.val, neighbors = [])
            seen[current.val] = copy
            for index in current.neighbors:
                copy.neighbors.append(helper(index,None))
            return copy
        return helper(node,None)