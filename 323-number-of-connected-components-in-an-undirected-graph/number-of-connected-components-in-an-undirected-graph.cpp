class Solution {
public:
    void bfs(vector<int>& visited, vector<vector<int>>& graph,int vertex, int& comp_count){
        queue<int> q;
        q.push(vertex);
        while(!q.empty()){
            int curr = q.front();
            q.pop();
            visited[curr] = 1;
            for(int neighbor: graph[curr]){
                if (visited[neighbor] == 0){
                    q.push(neighbor);
                    visited[neighbor] = 1;
                }
            }
        }
    }
    void dfs(vector<int>& visited, vector<vector<int>>& graph,int vertex, int& comp_count){
        if (visited[vertex] == 1){
            return;
        }
        visited[vertex] = 1;
        for(auto neighbor: graph[vertex]){
            dfs(visited, graph, neighbor, comp_count);
        }
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> graph(n);
        vector<int> visited(n);
        int comp_count = 0;
        for(int index = 0; index < edges.size(); index++){
            vector<int> curr = edges[index];
            graph[curr[0]].push_back(curr[1]);
            graph[curr[1]].push_back(curr[0]);
        }
        for(int vertex = 0; vertex < n; vertex++){
            if(visited[vertex] == 0){
                comp_count++;
                bfs(visited,graph,vertex,comp_count);
            }
        }
        return comp_count;
    }
};