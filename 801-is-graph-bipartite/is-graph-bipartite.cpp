class Solution {
public:
    bool bfs(vector<vector<int>>& graph,vector<int>& visited,vector<int>& color, int parent, int paint, int vertex){
        //{{vertex, parent}, paint}
        queue<pair<pair<int, int>, int>> q;
        q.push({{vertex, -1}, 1});
        visited[vertex] = 1;
        color[vertex] = paint;
        while(!q.empty()){
            int vertex = q.front().first.first;
            int parent = q.front().first.second;
            int paint = q.front().second;
            q.pop();
            for(int neighbor: graph[vertex]){
                if (neighbor == parent){
                    continue;
                }
                if (visited[neighbor] == 0){
                    q.push({{neighbor, vertex}, paint == 1? 2: 1});
                    visited[neighbor] = 1;
                    color[neighbor] = paint == 1? 2: 1;
                }else if(color[neighbor] == paint){
                    return false;
                }
            }
        }
        return true;
    }

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