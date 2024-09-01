class Solution {
public:
    vector<int> bfs(vector<vector<int>>& graph, int V,vector<int>& indegree, vector<int>& visited){
        queue<int> q;
        vector<int> ans;
        for(int vertex = 0; vertex < V; vertex++){
            if (indegree[vertex] == 0){
                q.push(vertex);
                ans.push_back(vertex);
                visited[vertex] = 1;
            }
        }
        while(!q.empty()){
            int vertex = q.front();
            q.pop();
            for(int neighbor: graph[vertex]){
                indegree[neighbor] -= 1;
                if (indegree[neighbor] == 0){
                    ans.push_back(neighbor);
                    q.push(neighbor);
                    visited[neighbor] = 1;
                }
            }
        }
        reverse(ans.begin(), ans.end());
        return ans.size() == V ? ans: vector<int>();
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> indegree(numCourses);
        vector<vector<int>> graph(numCourses);
        vector<int> visited(numCourses);
        for(vector<int> connection: prerequisites){
            int start = connection[0];
            int end = connection[1];
            indegree[end]++;
            graph[start].push_back(end);
        }
        return bfs(graph, numCourses, indegree, visited);
    }
};