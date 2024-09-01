class Solution {
public:
    bool dfs(vector<vector<int>>& graph,vector<int>& visited,vector<int>& color, int parent, int paint, int vertex){
        visited[vertex] = 1;
        color[vertex] = paint;
        for(int neighbor: graph[vertex]){
            if(visited[neighbor] == 0){
                if(!dfs(graph, visited, color,vertex, paint == 1 ? 2: 1, neighbor)){
                    return false;
                }
            }else if (color[neighbor] == paint){
                return false;
            }
        }
        return true;
    }
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n,0);
        vector<int> visited(n,0);
        for(int vertex=0; vertex < n; vertex++){
            if(visited[vertex] == 0){
                if(!dfs(graph, visited, color, -1, 1, vertex)){
                    return false;
                }
            }
        }
        return true;
    }
};