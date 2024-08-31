class Solution {
public:
    void dfs(vector<vector<int>>& graph,vector<int>& visited, int vertex){
        if (visited[vertex] == 1){
            return;
        }
        int n = graph.size();
        visited[vertex] = 1;
        for(int neighbor = 0; neighbor < n; neighbor++){
            if (graph[vertex][neighbor] == 1){
                dfs(graph, visited, neighbor);
            }
        }
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = isConnected.size();
        vector<int> visited(n);
        int ans = 0;
        for(int vertex = 0; vertex < n; vertex++){
            if(visited[vertex] == 0){
                ans++;
                dfs(isConnected, visited, vertex);
            }
        }
        return ans;
    }
};