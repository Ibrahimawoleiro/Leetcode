class Solution {
public:
    int bfs(vector<vector<int>>& grid){
        int row_size = grid.size();
        int col_size = grid[0].size();
        //create a queue to help keep track of rotten oranges
        // {{row, col}, time}
        queue<pair<pair<int, int>, int>> q;
        //Loop through the 2D array to look for the first rotten oranges
        for(int r = 0; r < row_size; r++){
            for(int c = 0; c < col_size; c++){
                if(grid[r][c] == 2){
                    q.push({{r,c}, 0});
                }
            }
        }
        vector<vector<int>> visited(row_size, vector<int>(col_size, -1));
        //Now we try to get the maximum time needed to rot all oranges
        int time = 0;

        while(!q.empty()){
            int r = q.front().first.first;
            int c = q.front().first.second;
            int t = q.front().second;
            time = max(time, t);
            q.pop();
            
            if (r - 1 >= 0 && grid[r - 1][c] == 1){
                q.push({{r - 1,c}, t + 1});
                grid[r - 1][c] = 2;
            }
            if (r + 1 < grid.size() && grid[r + 1][c] == 1){
                q.push({{r + 1,c}, t + 1});
                grid[r + 1][c] = 2;
            }
            if( c - 1 >= 0 && grid[r][c - 1] == 1){
                q.push({{r,c - 1}, t + 1});
                grid[r][c - 1] = 2;
            }
            if( c + 1 < grid[0].size() && grid[r][c + 1] == 1){
                q.push({{r,c + 1}, t + 1});
                grid[r][c + 1] = 2;
            }      
        }
        for(vector<int> arr: grid){
            for(int num: arr){
                if (num == 1){
                    return -1;
                }
            }
        }
        return time;
    }
    int orangesRotting(vector<vector<int>>& grid) {
        return bfs(grid);
    }
};