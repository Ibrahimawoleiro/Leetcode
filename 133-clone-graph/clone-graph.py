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
        if not node:
            return node
        elif len(node.neighbors) == 0:
            return Node(node.val)
        dic = {}
        dic_neighbors = {}
        visited = set()
        def helper(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in node.neighbors:
                #If the neigbor is already in seen neighbors of node.val
                if node.val in dic_neighbors:
                    if neighbor.val in dic_neighbors[node.val]:
                        continue
                    #If the record of the node is not in the dic
                if node.val not in dic:
                    #Create a new storage for current
                    dic[node.val] = []
                    dic[node.val].append(neighbor.val)
                    dic_neighbors[node.val] = set()
                    dic_neighbors[node.val].add(neighbor.val)
                    #If the neigbor isn't present in dic, create a new storage for it 
                    if neighbor.val not in dic:
                        dic[neighbor.val] = []
                        dic[neighbor.val].append(node.val)
                        dic_neighbors[neighbor.val] = set()
                        dic_neighbors[neighbor.val].add(node.val)
                    #If the neighbor is already in dic
                    else:
                        dic[neighbor.val].append(node.val)
                        dic_neighbors[neighbor.val].add(node.val)


                #If the record of the node is already in the dic
                else:
                    dic[node.val].append(neighbor.val)
                    dic_neighbors[node.val].add(neighbor.val)

                    #If the neigbor isn't present in dic, create a new storage for it 
                    if neighbor.val not in dic:
                        dic[neighbor.val] = []
                        dic[neighbor.val].append(node.val)
                        dic_neighbors[neighbor.val] = set()
                        dic_neighbors[neighbor.val].add(node.val)
                    else:
                        dic[neighbor.val].append(node.val)
                        dic_neighbors[neighbor.val].add(node.val)
                helper(neighbor)
        helper(node)
        #Now we model the relationships
        seen = {}
        
        def joiner(val):
            if val in seen:
                return seen[val]
            curr = Node(val, [])
            seen[val]=curr
            for n in dic[val]:
                curr.neighbors.append(joiner(n))
            return curr

        

        print("visited",visited)
        print("dic",dic)
        print("dic_neighbor",dic_neighbors)
        return joiner(1)
