class Solution {
    public boolean checkIfExist(int[] arr) {
        Set<Integer> set = new HashSet<Integer>();
        int i = 0;
        while(i<arr.length){
            if(((set.contains(arr[i]/2)) && arr[i] % 2 == 0) || set.contains(arr[i]*2)){
                return true;
            }
            set.add(arr[i]);
            i++;
        }
        return false;
    }
}