class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int f = image[sr][sc];
        recursive(sr,sc,f,color,image);
        return image;
    }

    void recursive(int r, int c,int f, int i, int[][] arr){
        if(r<0 || r>= arr.length || c<0 || c>= arr[0].length || arr[r][c] != f || arr[r][c] == i){
            return ;
        }

        arr[r][c] = i;
        recursive(r-1,c,f,i,arr);
        recursive(r+1,c,f,i,arr);
        recursive(r,c-1,f,i,arr);
        recursive(r,c+1,f,i,arr);
    }
}