class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        for(char c: s.toCharArray()){
            if(!stack.isEmpty() && stack.peek() == c){
                stack.pop();
                continue;
            }
            stack.push(c);
        }
        ArrayList<Character> storage = new ArrayList<>();
        while(!stack.isEmpty()){
            storage.add(stack.pop());
        }
        int i = 0;
        int j = storage.size() - 1;
        while(i <= j){
            char temp = storage.get(j);
            storage.set(j, storage.get(i));
            storage.set(i, temp);
            i++;
            j--;
        }
        String result = "";
        for(char c: storage){
            result += c;
        }
        return result;
    }
}