class Solution:
    def isPathCrossing(self, path: str) -> bool:
        store = {(0,0)}
        curr = [0,0]
        for index in range(len(path)):
            if path[index] == 'N':
                curr[0] += 1
                if tuple(curr) in store:
                    return True
                store.add(tuple(curr))
            elif path[index] == 'S':
                curr[0] -= 1
                if tuple(curr) in store:
                    return True
                store.add(tuple(curr))
            elif path[index] == 'E':
                curr[1] += 1
                if tuple(curr) in store:
                    return True
                store.add(tuple(curr))
            else:
                curr[1] -= 1
                if tuple(curr) in store:
                    return True
                store.add(tuple(curr))
            
        return False
