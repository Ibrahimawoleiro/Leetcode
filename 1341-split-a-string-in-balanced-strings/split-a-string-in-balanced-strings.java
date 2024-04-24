class Solution {
    public int balancedStringSplit(String s) {
        int r_count = 0;
        int l_count = 0;
        char[] helper = s.toCharArray();
        int r = 0;
        int l = 0;
        int ans = 0;

        while(r < helper.length){
            if(l == r){
                if (helper[r] == 'L'){
                    l_count += 1;
                }else{
                    r_count += 1;
                }
                r+=1;
                continue;
            }

            if (helper[r] == 'L'){
                l_count += 1;
            }else{
                r_count += 1;
            }
            
            if(r_count == l_count){
                System.out.println("l "+l+" r "+r);
                ans+=1;
                l_count = 0;
                r_count = 0;
                r += 1;
                l = r;
            }else{
                r+=1;
            }
            
        }
        return ans;
    }
}