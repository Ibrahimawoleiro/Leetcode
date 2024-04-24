class Solution {
    public int longestPalindrome(String s) {
        int odd = 0;
        int max_odd = 0;
        int total = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        for(char c: s.toCharArray()){
            if(!map.containsKey(c)){
                map.put(c, 1);
            }else{
                map.put(c, map.get(c) + 1);
            }
        }

        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            char key = entry.getKey();
            Integer value = entry.getValue();
            if(value % 2 == 0){
                total += value;
            }else{
                if(odd == 0){
                    odd+= 1;
                }
                
                total += value - 1;
            }
        }

        total+=odd;

        return total;
    }
}