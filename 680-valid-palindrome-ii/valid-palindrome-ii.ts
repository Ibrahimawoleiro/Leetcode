function validPalindrome(s: string): boolean {

    function recursive(f:number,b:number,chances: number): boolean {
        if (f==b || f>b){
            return true
        }
        if(s[f] == s[b]){
            return recursive(f+1,b-1,chances)
        }else{
            if(chances <= 0){
                return false
            }
            let try1: boolean = recursive(f+1,b,chances - 1)
            if (try1){
                return true
            }
            let try2: boolean = recursive(f, b - 1, chances - 1)
            if(try2){
                return true
            }
            return false
        }

    }

    return recursive(0, s.length - 1, 1)
    
};

