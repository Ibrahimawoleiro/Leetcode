function addStrings(num1: string, num2: string): string {
    let num1_last : number = num1.length - 1;
    let num2_last : number = num2.length - 1;
    let ans: string[] = [];
    let remainder: number = 0;
    while(num1_last >= 0 || num2_last >= 0){
        if (num1_last >= 0 && num2_last >= 0){
            const s1: string = num1.charAt(num1_last);
            const s2: string = num2.charAt(num2_last);
            let curr: number = parseInt(s1) + parseInt(s2) + remainder;
            if(curr >= 10){
                remainder = 1;
                curr = curr % 10;
            }else{
                remainder = 0;
            }
            ans.push(`${curr}`);
            num1_last--;
            num2_last--;
        }else if (num1_last >= 0){
            const s1: string = num1.charAt(num1_last);
            let curr: number = parseInt(s1) + remainder;
             if(curr >= 10){
                remainder = 1;
                curr = curr % 10;
            }else{
                remainder = 0;
            }
            ans.push(`${curr}`);
            num1_last--;
        }else{
            const s2: string = num2.charAt(num2_last);
            let curr: number = parseInt(s2) + remainder;
             if(curr >= 10){
                remainder = 1;
                curr = curr % 10;
            }else{
                remainder = 0;
            }
            ans.push(`${curr}`);
            num2_last--;
        }
    }
    if(remainder > 0){
        ans.push(`${remainder}`)
    }
    let result : string[] = ans.reverse();
    return result.join("")
};