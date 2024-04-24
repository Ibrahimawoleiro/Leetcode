class Solution {
    func getMaximumGenerated(_ n: Int) -> Int {
        if n == 0 {
            return 0;
        }
        var nums : [Int ] = Array(repeating: 0, count: n + 1);
        nums[1] = 1
        var i : Int = 0;

        while(i < nums.count){
            if 2 <= 2 * i && 2 * i <= n {
                nums[2 * i] = nums[i];
            }
            if 2 <= 2 * i + 1 && 2 * i + 1 <= n {
                nums[2 * i + 1] = nums[i] + nums[i + 1];
            }
            i+=1;
        }
        print(nums)
        return nums.max()!
    }
}