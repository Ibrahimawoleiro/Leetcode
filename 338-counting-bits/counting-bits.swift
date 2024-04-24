class Solution {
    func countBits(_ n: Int) -> [Int] {
        var store : [Int] = Array(repeating:0, count:n+1);
        var r: Int = 0;
        var helper: Int = 0;
        var x: Int = 2;
        while(r <= n){
            if r == 0{
                r+=1;
                helper += 1;
                continue;
            }
            if r == x{
                helper = x;
                x = x * 2;
            }
            store[r] = 1 + store[r - helper];
            r+=1;
        }
        return store;
    }
}