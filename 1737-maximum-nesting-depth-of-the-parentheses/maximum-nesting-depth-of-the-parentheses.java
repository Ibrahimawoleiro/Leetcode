class Solution {
    public int maxDepth(String s) {
        int max_count = 0;
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(c == '('){
                stack.push('(');
                if(stack.size() > max_count){
                    max_count = stack.size();
                }
            }else if (c == ')'){
                stack.pop();
            }else{
                continue;
            }
        }
        return max_count;
    }
}