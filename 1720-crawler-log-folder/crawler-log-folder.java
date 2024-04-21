class Solution {
    public int minOperations(String[] logs) {
        Stack<String> stack = new Stack<>();
        for(String f: logs){
            if(stack.isEmpty() && !f.equals("./") && !f.equals("../")){
                stack.push(f);
            }else if(f.equals("./") || !stack.isEmpty() && stack.peek().equals("./") ){
                continue;
            }else if(f.equals("../") ){
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }else if(!f.equals("./") && !f.equals("../")){
                stack.push(f);
            }
        }
        return stack.size();
    }
}