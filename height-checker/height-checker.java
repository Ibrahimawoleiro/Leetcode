class Solution {
    public int heightChecker(int[] heights) {
        int[] expected = new int[heights.length];
        int notmatch=0;
        for(int i=0; i<expected.length; i++){
            expected[i]=heights[i];
        }
        Arrays.sort(heights);
        for(int i=0; i<expected.length; i++){
            if(expected[i]!=heights[i]){
                notmatch++;
            }
        }
        return notmatch;
    }
}