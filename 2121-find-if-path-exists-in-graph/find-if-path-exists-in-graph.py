class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dictionary={}
        for connection in edges:
            if connection[0] not in dictionary:
                if connection[1] not in dictionary:
                        dictionary[connection[1]]=[connection[0]]
                        dictionary[connection[0]]=[connection[1]]
                elif connection[1] in dictionary:
                    dictionary[connection[0]]=[connection[1]]
                    dictionary[connection[1]].append(connection[0])
            elif connection[1] not in dictionary:
                if connection[0] not in dictionary:
                    dictionary[connection[1]]=[connection[0]]
                    dictionary[connection[0]]=[connection[1]]
                elif connection[0] in dictionary:
                    dictionary[connection[1]]=[connection[0]]
                    dictionary[connection[0]].append(connection[1])
            elif connection[0] in dictionary and connection[1] in dictionary:
                dictionary[connection[1]].append(connection[0])
                dictionary[connection[0]].append(connection[1])

        seen = set()
        isVisited = set()
        direction = []

        direction.append(source)
        while(direction):
            curr = direction.pop()
            if curr == destination:
                return True
            if curr not in isVisited:
                isVisited.add(curr)
                for neighbor in dictionary[curr]:
                    if neighbor not in seen:
                        direction.append(neighbor)
                        seen.add(neighbor)
        

        return False