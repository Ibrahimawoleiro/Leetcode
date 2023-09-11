class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dict = {}
        for connection in edges:
            if connection[0] not in dict:
                dict[connection[0]] = [connection[1]]
                print(dict[connection[0]] )
            else:
                dict[connection[0]].append(connection[1])
                
            if connection[1] not in dict:
                dict[connection[1]] = [connection[0]]
            else:
                dict[connection[1]].append(connection[0])
            
        seen = set()
        stack = []
        stack.append(source)
        while stack:
            curr = stack.pop()
            if curr in dict:
                for connection in dict[curr]:
                    if connection not in seen:
                        stack.append(connection)
            seen.add(curr)
            
            if(curr == destination):
                return True
        
        return False
            
            