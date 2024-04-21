class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        HashMap<Integer,Integer> store = new HashMap<>();
        int[] ans = new int[nums1.length];
        int e = nums2.length - 1;
        while(e >= 0){
            if(stack.isEmpty()){
                stack.push(nums2[e]);
                store.put(nums2[e], -1);
            }else{
                while(!stack.isEmpty() && stack.peek() <= nums2[e]){
                    System.out.println(stack.peek());
                    stack.pop();
                }
                if(stack.isEmpty()){
                    stack.push(nums2[e]);
                    store.put(nums2[e], -1);
                }else{
                    
                    System.out.println("stack"+stack.peek()+"curr"+nums2[e]);
                    store.put(nums2[e], stack.peek());
                    stack.push(nums2[e]);
                }
            }
            e-=1;
        }
        for(int i = 0; i < nums1.length; i++){
            ans[i] = store.get(nums1[i]);
        }
        return ans;
    }
}