class Solution {
    func moveZeroes(_ nums: inout [Int]) {
        var i: Int = 0

        var j: Int = 0
        while j < nums.count{
            if (nums[j] != 0) && (nums[i] == 0) {
                nums[i] = nums[j]
                nums[j] = 0
            }
            if(nums[i] != 0){
                i+=1
            }
            j+=1
        }
    }
}