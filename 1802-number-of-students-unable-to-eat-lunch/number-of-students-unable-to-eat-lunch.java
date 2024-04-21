class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int one_students = 0;
        int zero_students = 0;
        int i = 0;
        for(int n: students){
            if(n == 1){
                one_students+=1;
            }else{
                zero_students+=1;
            }
        }
        while(i < sandwiches.length){
            int curr = sandwiches[i];
            if((curr == 0 && zero_students == 0) || (curr == 1 && one_students == 0)){
                return one_students + zero_students;
            }else if(curr == 0){
                i+=1;
                zero_students -= 1;
            }else{
                i+=1;
                one_students -= 1;
            }
        }

        return 0;
    }
}