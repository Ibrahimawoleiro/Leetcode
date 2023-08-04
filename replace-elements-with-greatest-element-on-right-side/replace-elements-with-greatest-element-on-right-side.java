class Solution {
    public int[] replaceElements(int[] arr) {
        int max=arr[arr.length-1];
        for(int i = arr.length-1; i>=0; i--){
            if(i==arr.length-1){
                arr[i] = -1;
            }else{
                int temp = arr[i];
                arr[i]=max;
                if(temp>max){
                    max=temp;
                }
            }
        }
        return arr;
    }
}