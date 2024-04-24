class Solution {
    func tribonacci(_ n: Int) -> Int {
        var store : [Int : Int] = [Int : Int]();
        store[0] = 0;
        store[1] = 1;
        store[2] = 1;

        if n == 0 {
            return 0
        }else if n == 1 || n == 2 {
            return 1
        }

        func helper(curr number: Int) -> Int{
            if store.keys.contains(number){
                return store[number]!
            }
            var x: Int = helper(curr: number - 1) + helper(curr: number - 2) + helper(curr: number - 3)
            store[number] = x
            return x;
        }

        return helper(curr: n);
    }
}