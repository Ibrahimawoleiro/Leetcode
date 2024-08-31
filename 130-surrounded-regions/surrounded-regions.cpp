class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int row_size = board.size();
        int col_size = board[0].size();
        queue<pair<int,int>> q;
        for(int r = 0; r < row_size; r++){
            if(board[r][0] == 'O'){
                q.push({r, 0});
                board[r][0] = 'D';
            }
        }
        for(int r = 0; r < row_size; r++){
            if(board[r][col_size - 1] == 'O'){
                q.push({r, col_size - 1});
                board[r][col_size - 1] = 'D';
            }
        }
        for(int c = 0; c < col_size; c++){
            if(board[0][c] == 'O'){
                q.push({0,c});
                board[0][c] = 'D';
            }
        }
        for(int c = 0; c < col_size; c++){
            if(board[row_size - 1][c] == 'O'){
                q.push({row_size - 1,c});
                board[row_size - 1][c] = 'D';
            }
        }

        while(!q.empty()){
            int r = q.front().first;
            int c = q.front().second;
            q.pop();
            if(r - 1 >= 0 && board[r-1][c] == 'O'){
                q.push({r-1, c});
                board[r - 1][c] = 'D';
            }
            if(r + 1 < row_size && board[r+1][c] == 'O'){
                q.push({r+1, c});
                board[r+1][c] = 'D';
            }
            if(c - 1 >= 0 && board[r][c-1] == 'O'){
                q.push({r,c-1});
                board[r][c-1] = 'D';
            }
            if(c + 1 < col_size && board[r][c+1] == 'O'){
                q.push({r,c+1});
                board[r][c+1] = 'D';
            }
        }
        for(int r = 0; r < row_size; r++){
            for(int c = 0; c < col_size; c++){
                if(board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
            }
        }
        for(int r = 0; r < row_size; r++){
            for(int c = 0; c < col_size; c++){
                if(board[r][c] == 'D'){
                    board[r][c] = 'O';
                }
            }
        }
    }
};