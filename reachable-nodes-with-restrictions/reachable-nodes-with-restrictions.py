class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        dict = {}
        restrict = set()
        for val in restricted:
            restrict.add(val)
        
        for connection in edges:
            if connection[0] not in dict and (connection[0] not in restrict and connection[1] not in restrict):
                dict[connection[0]] = [connection[1]]
            elif (connection[0] not in restrict and connection[1] not in restrict):
                dict[connection[0]].append(connection[1])
            if connection[1] not in dict and (connection[0] not in restrict and connection[1] not in restrict):
                dict[connection[1]] = [connection[0]]
            elif (connection[1] not in restrict and connection[0] not in restrict):
                dict[connection[1]].append(connection[0])
         
      
        seen = set()
        stack = []   
        node_count = 0
        stack.append(0)
        while stack:
            print(stack)
            curr = stack.pop()
            if curr not in seen:
                seen.add(curr)
                node_count+=1
                if curr in dict:
                    for node in dict[curr]:
                        if node not in seen:
                            stack.append(node)
        
        return node_count
                    
                        