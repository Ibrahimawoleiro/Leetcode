class Solution {
    func climbStairs(_ n: Int) -> Int {
        if n == 1{
            return 1;
        }
        var store: [Int: Int] = [Int : Int]();
        var x : Int = 1;
        func helper(_ x : Int) -> Int{
            if x == 0 || x == 1 || store.keys.contains(x){
                if let curr = store[x]{
                    return curr;
                }
                return 1;
            }
            var curr: Int = helper(x-1) + helper(x-2);
            store[x] = curr;
            return curr;
        }

        var closure: (Int) -> Int = { (x : Int) -> Int in
            return helper(x);
        }

        return closure(n);
        
    }
    
}