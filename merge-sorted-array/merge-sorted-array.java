class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[nums1.length];
        if((nums1.length == 0 && nums2.length == 0) || (nums1.length == 0 && nums2.length>0) || (nums1.length>0 && nums2.length == 0) || n==0){
            return;
        }
        if(nums1.length==n && nums2.length >0){
            for(int i = 0; i<nums1.length; i++){
                nums1[i]=nums2[i];
            }
            return;
        }
        int i=0,j = 0,k=0;
        while((j<nums1.length || k<nums2.length) && i<temp.length){
            if(j<nums1.length && k<nums2.length){
                if((nums1[j] < nums2[k]) && j<m){
                    temp[i]=nums1[j];
                    i++;
                    j++;
                    continue;
                }
                temp[i]=nums2[k];
                    i++;
                    k++;
            }else if(j<m){
                temp[i]=nums1[j];
                i++;
                j++;
                
            }else if(k<nums2.length){
                temp[i]=nums2[k];
                i++;
                k++;
                continue;
            }
        }
        for(i=0; i<temp.length; i++){
            nums1[i]=temp[i];
        }
        
    }
}