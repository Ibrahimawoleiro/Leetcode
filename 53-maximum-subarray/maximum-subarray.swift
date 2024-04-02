class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        // //1
        // var maximum:Int = -Int(pow(10.0,5.0))
        // for i in 0..<nums.count{
        //     var current_sum = nums[i]
        //     for j in i..<nums.count{
        //         if i == j{
        //             if nums[i] > maximum{
        //                 maximum = nums[i]
                        
        //             }
        //             continue
        //         }
        //         current_sum += nums[j]
        //         if current_sum > maximum{
        //             maximum = current_sum
        //             print(maximum)
        //         }
        //     }
        // }
        // return maximum

        //2

        var maximum = -Int(pow(10.0,5.0))
        var current_sum = 0
        print(nums.count)
        for index in stride(from:0, to: nums.count, by:1){
            if current_sum + nums[index] > nums[index]{
                current_sum += nums[index]
            }else{
                current_sum = nums[index]
            }
            if current_sum > maximum{
                maximum = current_sum
            }
        }
        return maximum
    }
}