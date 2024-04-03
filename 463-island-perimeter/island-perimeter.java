class Solution {
    public int islandPerimeter(int[][] grid) {
        boolean islandSeen = false;
        int r = 0; 
        int c = 0;
        while(islandSeen == false && r < grid.length){
            while(c < grid[0].length){
                if(grid[r][c] == 1){
                    islandSeen = true;
                    return recursive(r,c, grid);
                }
                c++;
            }
            c=0;
            r++;
        }
        return 0;
    }
    public int recursive(int r, int c, int[][] grid){
        if (r<0 || r >= grid.length || c<0 || c >= grid[0].length || grid[r][c] == 0){
            return 1;
        }else if(grid[r][c] != 0 && grid[r][c] != 1){
            return 0;
        }
        System.out.println("Row "+r+"Column "+ c);
        grid[r][c] = 5;
        return recursive(r-1,c,grid) + recursive(r+1,c,grid) + recursive(r,c+1,grid) + recursive(r,c-1,grid);
    }
}