class Solution {
    public boolean validMountainArray(int[] arr) {
        if(arr.length <3){
            return false;
        }
        boolean rising=false;
        boolean falling=false;
        for(int i=1; i<arr.length;i++){
            if(arr[i-1]==arr[i]){
                return false;
            }
            if(arr[i-1]<arr[i]){
                if(rising==false && falling==false){
                    rising=true;
                }else if(rising==true && falling==false){
                    continue;
                }else if((rising==true || rising==false ) && falling==true){
                    return false;
                }
            }
            if(arr[i-1]>arr[i]){
                if(rising==true && falling==false){
                    falling=true;
                }else if(falling==false && (rising==true || rising == false)){
                    return false;
                }
            }
        }
        if(rising == true && falling ==false){
            return false;
        }
        return true;
    }
}