class Solution {
public:
    
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        queue<pair<int, int>> q;
        int target_color = image[sr][sc];
        q.push({sr, sc});
        vector<vector<int>> visited(image.size(), vector<int>(image[0].size(), -1));
        visited[sr][sc] = 1;
        while(!q.empty()){
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            image[r][c] = color;

            if (r - 1 >= 0 && image[r - 1][c] == target_color && visited[r - 1][c] == -1){
                image[r - 1][c] = color;
                visited[r - 1][c] = 1;
                q.push({r - 1,c});
            }
            if (r + 1 < image.size() && image[r + 1][c] == target_color && visited[r + 1][c] == -1){
                image[r + 1][c] = color;
                visited[r + 1][c] = 1;
                q.push({r + 1,c});
            }
            if(c - 1 >= 0 && image[r][c - 1] == target_color && visited[r][c - 1] == -1){
                image[r][c - 1] = color;
                visited[r][c - 1] = 1;
                q.push({r, c - 1});
            }
            if(c + 1 < image[0].size() && image[r][c + 1] == target_color && visited[r][c + 1] == -1){
                image[r][c + 1] = color;
                visited[r][c + 1] = 1;
                q.push({r, c + 1});
            }
        }
        return image;
    }
};