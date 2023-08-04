class Solution {
    public void duplicateZeros(int[] arr) {
        int[] result = new int[arr.length];
        int resultCounter=0;
        for(int i = 0; i<arr.length && resultCounter<=arr.length-1; i++){
            if(arr[i]!=0){
                result[resultCounter]=arr[i];
                resultCounter++;
            }else{
                if(resultCounter<arr.length){
                    result[resultCounter]=0;
                }
                if(resultCounter+1<arr.length){
                    result[resultCounter+1]=0;
                }
                resultCounter +=2;
            }
        }
        for(int i=0; i<arr.length; i++){
            arr[i]=result[i];
        }
    }
}