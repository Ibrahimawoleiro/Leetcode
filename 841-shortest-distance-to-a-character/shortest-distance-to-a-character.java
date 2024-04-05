class Solution {
    public int[] shortestToChar(String s, char c) {
        int[] ans = new int[s.length()];
        Arrays.fill(ans,(int)Math.pow(10,5));
        for(int j = 0; j<s.length(); j++){
            if(s.charAt(j) == c){
                int i = j - 1;
                ans[j] = 0;
                int count = 1;
                while(i>=0){
                    if (s.charAt(i) == c){
                        break;
                    }
                    if(count < ans[i]){
                        ans[i] = count;
                    }
                    count+=1;
                    i-=1;
                }
                i = j + 1;
                count = 1;
                while(i<s.length()){
                    if (s.charAt(i) == c){
                        break;
                    }
                    if(count < ans[i]){
                        ans[i] = count;
                    }
                    count+=1;
                    i+=1;
                }
            }
        }
        return ans;
    }
}