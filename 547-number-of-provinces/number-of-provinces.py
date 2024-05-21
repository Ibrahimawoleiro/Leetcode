class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        visited = [0 for i in range(len(isConnected))]
        count = 0
        def dfs(i):
            if visited[i] == 1:
                return 
            visited[i] = 1

            for c in range(len(isConnected[i])):
                if isConnected[i][c] == 1:
                    dfs(c)


        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if visited[r] == 0:
                    count += 1
                    dfs(r)
        
        return count
                
