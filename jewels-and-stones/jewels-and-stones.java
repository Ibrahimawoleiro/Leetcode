class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashSet<Character> jewelSet=new HashSet();  
        for(char c: jewels.toCharArray()){
            if(!jewelSet.contains(c)){
                jewelSet.add(c);
            }
        }
        int count = 0;
        for(char c: stones.toCharArray()){
            if(jewelSet.contains(c)){
                count++;
            }
        }
        return count;
    }
}