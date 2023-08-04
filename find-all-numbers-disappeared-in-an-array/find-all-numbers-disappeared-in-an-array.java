class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
         List<Integer> l1 = new ArrayList<Integer>();
         Set<Integer> hash_Set = new HashSet<Integer>();
        for(int i=0; i<nums.length; i++){
            hash_Set.add(nums[i]);
        }
        for(int i=1; i<=nums.length; i++){
            if(!hash_Set.contains(i)){
                l1.add(i);
            }
        }
        return l1;
    }
}