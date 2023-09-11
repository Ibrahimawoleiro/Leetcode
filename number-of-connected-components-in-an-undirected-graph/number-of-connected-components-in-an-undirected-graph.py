class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        //Create the connections using a dictionaary
        //Create a stack. This would be needed for dfs
        //Component_count
        //Create a loop that runs from 0 to n-1
        //Create a set Seen
        // for each value in the loop
            //If there's a case where the current value is not in seen
            //Increase component count by 1
            //Check for its connected components using dfs
            
        """
        dict = {}
        
        for connection in edges:
            if connection[0] not in dict:
                dict[connection[0]] = [connection[1]]
            else:
                dict[connection[0]].append(connection[1])
            if connection[1] not in dict:
                dict[connection[1]] = [connection[0]]
            else:
                dict[connection[1]].append(connection[0])
                
                    
        stack = []
        seen = set()
        component_count = 0
        #print(dict)
        for val in range(n):
            if val not in seen:
                component_count+=1
                stack.append(val)
                while stack:
                    curr = stack.pop()
                    print(curr)
                    #print(seen)
                    seen.add(curr)
                    if curr in dict:
                        for connection in dict[curr]:
                            if connection not in seen:
                                stack.append(connection)
        
        return component_count


        