class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = (m - 1);
        int j = n - 1;
        int f = m + n - 1;
        System.out.println(f);
        while(f >= 0){
            if(i>=0 && j>=0){
                if (nums1[i] > nums2[j]){
                    nums1[f] = nums1[i];
                    i--;
                    f--;
                }else{
                    nums1[f] = nums2[j];
                    j--;
                    f--;
                }
            }else if(i < 0){
                nums1[f] = nums2[j];
                f--;
                j--;
            }else{
                nums1[f] = nums1[i];
                f--;
                i--;
            }
        }
    }
}